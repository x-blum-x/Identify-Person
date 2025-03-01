from scipy.spatial import distance

def bbox_distance(bbox1, bbox2):
    """Calcula a distância entre dois bounding boxes."""
    center1 = ((bbox1[0] + bbox1[2]) / 2, (bbox1[1] + bbox1[3]) / 2)
    center2 = ((bbox2[0] + bbox2[2]) / 2, (bbox2[1] + bbox2[3]) / 2)
    return distance.euclidean(center1, center2)

def is_bbox_out_of_frame(bbox, frame_width, frame_height):
    """Verifica se um bounding box está fora da tela."""
    x1, y1, x2, y2 = bbox
    return x2 < 0 or y2 < 0 or x1 > frame_width or y1 > frame_height

def average_bbox_distance(person, det_bbox):
    """Calcula a distância média entre o histórico de posições da pessoa e o bounding box detectado."""
    center2 = ((det_bbox[0] + det_bbox[2]) / 2, (det_bbox[1] + det_bbox[3]) / 2)
    distances = [distance.euclidean((x, y), center2) for (x, y) in person.position_history]
    return sum(distances) / len(distances)