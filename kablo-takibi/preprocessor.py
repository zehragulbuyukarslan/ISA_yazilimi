# preprocessor.py

def get_cable_offset(detections, frame_width):
    for det in detections:
        if det['class'] == 'cable':
            x1, _, x2, _ = det['bbox']
            cable_center = (x1 + x2) / 2
            frame_center = frame_width / 2
            return frame_center - cable_center
    return None