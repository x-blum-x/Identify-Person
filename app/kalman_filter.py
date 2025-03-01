import cv2
import numpy as np

class Person:
    def __init__(self, id, bbox, entry_time):
        self.id = id
        self.bbox = bbox  # (x1, y1, x2, y2)
        self.entry_time = entry_time
        self.last_seen = entry_time
        self.position_history = []  # Histórico de posições
        # Inicializar o filtro de Kalman
        self.kalman_filter = cv2.KalmanFilter(4, 2)
        self.kalman_filter.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
        self.kalman_filter.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
        self.kalman_filter.processNoiseCov = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.01
        # Calcular o centro do bounding box
        center_x = (bbox[0] + bbox[2]) / 2
        center_y = (bbox[1] + bbox[3]) / 2
        # Inicializar o estado do filtro de Kalman
        self.kalman_filter.statePre = np.array([[center_x], [center_y], [0], [0]], np.float32)
        self.kalman_filter.statePost = np.array([[center_x], [center_y], [0], [0]], np.float32)
        # Adicionar a posição inicial ao histórico
        self.position_history.append((center_x, center_y))