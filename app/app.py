import cv2
import torch
import time
import numpy as np
from config import DISTANCE_THRESHOLD, CONFIDENCE_THRESHOLD, MAX_TIME_UNSEEN
from tracker_utils import bbox_distance, is_bbox_out_of_frame, average_bbox_distance
from kalman_filter import Person

# Carregar o modelo YOLOv5 (usando um modelo maior para melhor precisão)
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # Usando YOLOv5m

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

def main():
    # Lista de pessoas detectadas e contador global de IDs
    tracked_persons = []
    next_person_id = 1
    # Lista para armazenar as informações das pessoas que saíram da tela
    exited_persons = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Obter resultados da detecção
        results = model(frame)
        
        # Obter o tempo atual
        current_time = time.time()

        # Lista de bounding boxes detectados no frame atual
        current_detections = []
        for det in results.xyxy[0]:
            x1, y1, x2, y2, conf, cls = det
            if int(cls) == 0 and conf > CONFIDENCE_THRESHOLD:  # Classe 0 é 'person' no modelo YOLOv5
                current_detections.append((int(x1), int(y1), int(x2), int(y2)))

        # Associar detecções aos objetos rastreados
        unmatched_detections = current_detections.copy()
        for person in tracked_persons:
            best_match = None
            min_dist = float('inf')
            
            # Procurar a detecção mais próxima
            for i, det_bbox in enumerate(unmatched_detections):
                dist = average_bbox_distance(person, det_bbox)  # Usar distância média
                if dist < min_dist and dist < DISTANCE_THRESHOLD:
                    min_dist = dist
                    best_match = i

            if best_match is not None:
                # Atualizar a posição e o último tempo visto
                person.bbox = unmatched_detections[best_match]
                person.last_seen = current_time
                # Atualizar o filtro de Kalman
                center_x = (person.bbox[0] + person.bbox[2]) / 2
                center_y = (person.bbox[1] + person.bbox[3]) / 2
                measurement = np.array([[center_x], [center_y]], np.float32)
                person.kalman_filter.correct(measurement)
                # Adicionar a nova posição ao histórico
                person.position_history.append((center_x, center_y))
                unmatched_detections.pop(best_match)
            else:
                # Prever a posição usando o filtro de Kalman
                prediction = person.kalman_filter.predict()
                predicted_center_x = int(prediction[0][0])  # Extrair o valor correto do array
                predicted_center_y = int(prediction[1][0])  # Extrair o valor correto do array
                # Atualizar o bounding box com base na previsão
                width = person.bbox[2] - person.bbox[0]
                height = person.bbox[3] - person.bbox[1]
                person.bbox = (
                    predicted_center_x - width // 2,
                    predicted_center_y - height // 2,
                    predicted_center_x + width // 2,
                    predicted_center_y + height // 2
                )

        # Adicionar novas pessoas detectadas
        for det_bbox in unmatched_detections:
            new_person = Person(next_person_id, det_bbox, current_time)
            tracked_persons.append(new_person)
            next_person_id += 1  # Incrementar a variável global

        # Remover pessoas que não foram vistas por um tempo maior que MAX_TIME_UNSEEN
        # ou que estão fora dos limites da tela
        for person in tracked_persons[:]:
            if (current_time - person.last_seen > MAX_TIME_UNSEEN or
                is_bbox_out_of_frame(person.bbox, frame.shape[1], frame.shape[0])):
                # Calcular o tempo total que a pessoa permaneceu na tela
                total_time = person.last_seen - person.entry_time
                # Adicionar à lista de pessoas que saíram
                exited_persons.append((person.id, total_time))
                # Remover da lista de pessoas rastreadas
                tracked_persons.remove(person)

        # Desenhar bounding boxes e informações no frame
        for person in tracked_persons:
            x1, y1, x2, y2 = person.bbox
            total_time = current_time - person.entry_time
            text = f'ID {person.id}: {total_time:.2f} s'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Exibir a lista de pessoas que saíram no canto superior direito da tela
        y_offset = 30
        for person_id, total_time in exited_persons:
            text = f'ID {person_id}: {total_time:.2f} s'
            cv2.putText(frame, text, (frame.shape[1] - 200, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            y_offset += 20

        # Mostrar o frame com as detecções
        cv2.imshow('YOLOv5 Person Tracking', frame)
        
        # Verificar se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Exibir o tempo total de permanência de cada pessoa
    for person in tracked_persons:
        total_time = person.last_seen - person.entry_time
        print(f'Pessoa ID {person.id} permaneceu visível por {total_time:.2f} segundos')

    # Liberar a captura de vídeo e fechar janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()