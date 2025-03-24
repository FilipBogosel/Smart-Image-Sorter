#================MAIN MODULE================

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
from configuration import  IMAGE_EXTENSIONS, DESTINATION_FOLDERS, NATURE_KEYWORDS
from helpers import initialize_folders
from detection import setup_detector, detect_people, detect_animals
from classification import classify_nature, classify_food, classify_urban, classify_art, classify_vehicle

def process_image(file_path, detector, source_folder):
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
            return os.path.join(source_folder, DESTINATION_FOLDERS['pet'])
        if person_count == 1:
            return os.path.join(source_folder, DESTINATION_FOLDERS['portrait'])
        elif person_count == 2:
            return os.path.join(source_folder, DESTINATION_FOLDERS['couple'])
        elif person_count > 2:
            return os.path.join(source_folder, DESTINATION_FOLDERS['group'])
        elif classify_food(file_path):
            return os.path.join(source_folder, DESTINATION_FOLDERS['food'])
        elif classify_art(file_path):
            return os.path.join(source_folder, DESTINATION_FOLDERS['art'])
        elif classify_vehicle(file_path):
            return os.path.join(source_folder, DESTINATION_FOLDERS['vehicle'])
        elif classify_urban(file_path):
            return os.path.join(source_folder, DESTINATION_FOLDERS['urban'])
        elif classify_nature(file_path):
            return os.path.join(source_folder,DESTINATION_FOLDERS['nature'])


        else:
            return os.path.join(source_folder, DESTINATION_FOLDERS['other'])
    except Exception as e:
        print(f"Error processing image: {e}")
        return os.path.join(source_folder, DESTINATION_FOLDERS['other'])

def organize_photos(source_folder):
    initialize_folders(source_folder)#create the folders we want to put our images in
    detector = setup_detector()# create the detector instance for people and animals objects

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isdir(file_path):# if the obtained path is one of a subfolder because we want only to analyse the files
            continue# we go to the next file/subfolder

        ext = os.path.splitext(filename)[1].lower()# splitext is a function that splits the path into a pair(root, ext),
        # where ext is the extension lowercase
        if ext not in IMAGE_EXTENSIONS:# if the file's extension doesn't match a photo's extension we set the destination as the non-photos folder
            dest = os.path.join(source_folder, DESTINATION_FOLDERS['non_photos'])
        else:
            dest = process_image(file_path, detector,source_folder)# we process the image to find the appropriate folder for it,
            # see the process_image function above for more details

        try:
            shutil.move(file_path, os.path.join(dest, filename))# move the file to the destination folder
            print(f"Moved {filename} to {os.path.basename(dest)}")# print a message to show that the file was moved
        except Exception as e:
            print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the path to the folder with the photos: ")# ask the user for the path to the folder with the photos
    organize_photos(source_folder)# call the function to organize the photos
    print("Done!")