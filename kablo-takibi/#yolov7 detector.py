#yolov7 detector.py

def detect_objects(frame):
    """
    Frame'i alır, YOLOv7 ile tespit yapar.
    Dummy veridir, gerçek model için torch modeli gerekir.
    """
    return [
        {'class': 'cable', 'bbox': [250, 200, 350, 300]},
        {'class': 'circle', 'bbox': [400, 250, 450, 300]}
    ]
