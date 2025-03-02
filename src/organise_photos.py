# I wrote comments to explain the code, so that anyone can understand what each part of the code does.
# I also wrote some theoretical comments to explain the concepts used in the code, concepts that I learned about when doing research for this project.
# The code is written in 5 modules: configuration.py, helpers.py, detection.py, classification.py, organise_photos.py, each with a specific role.
import os  # os module provides a way of using operating system functionalities
import shutil  # shutil module provides some functions to work with file objects and directories
import torch  # PyTorch is an open source machine learning library from which we will use the ResNet18 model
from PIL import Image  # PIL is the Python Imaging Library, which we will use to load images
# torchvision is a package in PyTorch that contains popular datasets, model architectures,
# and common image transformations for computer vision
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights  # import the ResNet18 model and its weights
# Important: An AI model's weights are the values that the model is using to make predictions,
# they are like arguments to a function. The weights are learned during the training of the model.
# Those weights are like the characteristics of the things that the model is trying to predict.
from imageai.Detection import ObjectDetection  # import the ObjectDetection class from the imageai.Detection module
#we import the configurations from the configuration.py file: the dictionaries for keywords for each category of photos, etc.
from configuration import SOURCE_FOLDER, IMAGE_EXTENSIONS, DESTINATION_FOLDERS, NATURE_KEYWORDS
from helpers import initialize_folders
from detection import setup_detector, detect_people, detect_animals
from classification import classify_nature, classify_food, classify_urban, classify_art, classify_vehicle

def process_image(file_path, detector):
    """Categorize the image.
    :param file_path: The path to the image file.
    :param detector: The detector object returned by setup_detector.
    :return: The destination folder for the image.
    """
    #try-except for error handling
    #the code in the try block finds the appropriate folder for the image, based on the content of the image, if the file is an image
    # It does so by checking in a bunch of if and elif statements the category of the image
    # And then using the appropriate folder from the DESTINATION_FOLDERS dictionary
    try:
        person_count = detect_people(detector, file_path)
        exists_animal = detect_animals(detector,file_path)
        if exists_animal and not(classify_nature(file_path)):
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['pet'])
        if person_count == 1:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['portrait'])
        elif person_count == 2:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['couple'])
        elif person_count > 2:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['group'])
        elif classify_nature(file_path):
            return os.path.join(SOURCE_FOLDER,DESTINATION_FOLDERS['nature'])
        elif classify_urban(file_path):
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['urban'])
        elif classify_food(file_path):
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['food'])
        elif classify_art(file_path):
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['art'])
        elif classify_vehicle(file_path):
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['vehicle'])
        else:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['other'])
    except Exception as e:
        print(f"Error processing image: {e}")
        return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['other'])

def organize_photos():
    initialize_folders()#create the folders we want to put our images in
    detector = setup_detector()# create the detector instance for people and animals objects

    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(filename)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            dest = os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['non_photos'])
        else:
            dest = process_image(file_path, detector)

        try:
            shutil.move(file_path, os.path.join(dest, filename))
            print(f"Moved {filename} to {os.path.basename(dest)}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    organize_photos()
    print("Done!")