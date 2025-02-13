# ===========CLASSIFICATION MODULE==========
#=====We'll have classification for nature images, urban images, food images, art images, vehicle images

import torch# PyTorch is an open source machine learning library from which we will use the ResNet18 model
from PIL import Image# PIL is the Python Imaging Library, which we will use to load images
from torchvision import transforms# torchvision is a package in PyTorch that contains popular datasets, model architectures and
# common image transformations for computer vision, from which we will use the transforms module, which provides common image transformations
# such as resizing, cropping, etc.
from torchvision.models import resnet18, ResNet18_Weights
from configuration import NATURE_KEYWORDS,FOOD_KEYWORDS,URBAN_KEYWORDS,ART_KEYWORDS,VEHICLE_KEYWORDS
from helpers import obtain_photo_category_label

#SHORT SUMMARY OF A CLASSIFICATION FUNCTION(All classification functions will have the same structure, a lot of code is in the helpers.py file):
#The function classify_nature(image_path) takes the path to an image file as input, loads the image, preprocesses it,
# and classifies it as a nature image or not.
# 1. Load ResNet18 model with ImageNet weights and set it to evaluation mode.
# 2. Initialise the preprocessing : resize it to 256x256 pixels, crop the center to 224x224 pixels, convert it to a tensor, and normalize it.
# 3. Load the image, preprocess it, and pass it through the model to get the output.
# 4. Process the output to get the class label with the highest probability.
# 5. Interpret the result: if the class label contains any of the nature keywords, return True, otherwise return False.

#NOTE: A normalization algorithm in general transforms a set of data in something that is actually interpretable


def classify_nature(image_path):
    """Checks for nature images using PyTorch's ResNet18.
    :param image_path: The path to the image file.
    :return: True if the image has nature content, False otherwise.
    """
    class_label = obtain_photo_category_label(image_path)#obtain the category label of the image
    return any(keyword in class_label.lower() for keyword in NATURE_KEYWORDS)#return True if any of the nature keywords is found in the class label,
# the class_label being a string so even if the keyword is a substring of the class label, it will return True, otherwise it will return False

def classify_urban(image_path):
    """Checks for urban(in thd city) images using PyTorch's ResNet18.
       :param image_path: The path to the image file.
       :return: True if the image has urban content, False otherwise.
       """
    class_label = obtain_photo_category_label(image_path)
    return any(keyword in class_label.lower() for keyword in URBAN_KEYWORDS)


def classify_food(image_path):
    """Checks for food images using PyTorch's ResNet18.
       :param image_path: The path to the image file.
       :return: True if the image has food content the most, False otherwise.
       """
    class_label = obtain_photo_category_label(image_path)
    return any(keyword in class_label.lower() for keyword in FOOD_KEYWORDS)

def classify_art(image_path):
    """Checks for art images using PyTorch's ResNet18.
       :param image_path: The path to the image file.
       :return: True if the image has art content, False otherwise.
       """
    class_label = obtain_photo_category_label(image_path)
    return any(keyword in class_label.lower() for keyword in ART_KEYWORDS)

def classify_vehicle(image_path):
    """Checks for vehicle images using PyTorch's ResNet18.
       :param image_path: The path to the image file.
       :return: True if the image has vehicle content, False otherwise.
       """
    class_label = obtain_photo_category_label(image_path)
    return any(keyword in class_label.lower() for keyword in VEHICLE_KEYWORDS)

