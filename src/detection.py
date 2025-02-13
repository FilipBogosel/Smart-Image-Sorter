# ============DETECTION MODULE================
#=====We'll have detection for people and animals
import os
from imageai.Detection import ObjectDetection# import the ObjectDetection class from the imageai.Detection module
from configuration import ANIMAL_KEYWORDS

def setup_detector()->ObjectDetection:
    """Initialize the people detector (RetinaNet).
    :return: The detector object.(The actual model that will be used to detect people in images)
    """
    #the dirname function returns the directory containing the file passed as an argument
    base_path = os.path.dirname(os.path.dirname(__file__))# get the parent directory of the current file, __file__ contains the path of the current file
    model_path = os.path.join(base_path, "models", "retinanet_resnet50_fpn_coco-eeacb38b (1).pth")
    # We build the path this way because the model is in the models folder, while the detection.py file is in the src folder
    detector = ObjectDetection()# create an instance of the ObjectDetection class
    detector.setModelTypeAsRetinaNet()# this method sets the model type to RetinaNet(a model for object detection, good on small objects)
    detector.setModelPath(model_path)# Tells the detector where to find: pre-trained weights(the parameters that are found to be
    # the best for the model in a previous training), Model architecture file(the structure of the model)
    detector.loadModel()# this method is the one that actually reads the model from the files and loads the weights in memory=> the model is ready to be used
    print("Detection model loaded!")
    return detector# return the detector object, of type ObjectDetection, ready to be used

def detect_people(detector, file_path):
    """Detect people in an image.
    :param detector: The detector object returned by setup_detector.
    :param file_path: The path to the image file.
    :return: The number of people detected in the image.
    """
    detections = detector.detectObjectsFromImage(
        input_image=file_path,# the path to the image file
        output_image_path=None,# we don't need to save the image with the detected objects highlighted
        minimum_percentage_probability=40# if the object detected has a probability of being a certain object greater than 40%, we consider it as being that object
    )# this method returns a list of dictionaries, each dictionary contains information about an object detected in the image
    return sum(1 for obj in detections if obj["name"] == "person")# goes through dictionaries and counts the number of people detected, each dictionary being an object found in the image

#TODO: Remember, if the image has an animal, even if it has people, it can't be portrait, couple or group, it will be classified as pet or nature
# if it has nature keywords(Do in organise_photos.py)

def detect_animals(detector, file_path):
    """
    Detect animals in an image
    :param detector: The detector object returned by setup_detector.
    :param file_path: The path to the image file.
    :return: True if an animal is detected in the image, False otherwise.
    """
    detections = detector.detectObjectsFromImage(
        input_image=file_path,
        output_image_path=None,
        minimum_percentage_probability=50
    )
    return any(obj["name"] in ANIMAL_KEYWORDS for obj in detections)# return True if any of the detected objects is an animal, otherwise return False

