# ============DETECTION MODULE================
import os
from imageai.Detection import ObjectDetection

def setup_detector():
    """Initialize the people detector (RetinaNet)."""
    base_path = os.path.dirname(os.path.dirname(__file__))
    model_path = os.path.join(base_path, "models", "retinanet_resnet50_fpn_coco-eeacb38b (1).pth")
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(model_path)
    detector.loadModel()
    print("Detection model loaded!")
    return detector

def detect_people(detector, file_path):
    """Detect people in an image."""
    detections = detector.detectObjectsFromImage(
        input_image=file_path,
        output_image_path=None,
        minimum_percentage_probability=40
    )
    return sum(1 for obj in detections if obj["name"] == "person")