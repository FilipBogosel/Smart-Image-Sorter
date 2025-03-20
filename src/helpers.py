# ========== HELPER FUNCTIONS MODULE========== #

import os
from configuration import DESTINATION_FOLDERS
import torch
from PIL import Image
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights

print(torch.cuda.is_available())
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # check if GPU is available, if not use CPU
# Important: The device is the hardware on which the model will run, it can be a CPU or a GPU, the GPU is faster than the CPU
print(f"Using computation device: {DEVICE}")


def initialize_folders(source_folder):
    """Create destination folders."""
    for folder in DESTINATION_FOLDERS.values():
        folder_path = os.path.join(source_folder, folder)# create the path for each folder
        os.makedirs(folder_path, exist_ok=True)# create the folder if it does not exist
    print("Folders created!")

def obtain_photo_category_label(image_path, top_n = 5):
    '''
    This function uses the ResNet18 model to classify an image into one of the 1000 categories from the ImageNet dataset.
    :param image_path: The path to the image file.
    :param top_n: The number of top categories to return, to make sure that we nailed the category.
    :return: The category label of the image.
    '''
    #Optimization for speed, load the model only once, not every time we call the function
    if not hasattr(obtain_photo_category_label, "model"):
        obtain_photo_category_label.model = resnet18(weights = ResNet18_Weights.IMAGENET1K_V1).to(DEVICE)
        obtain_photo_category_label.model.eval()
     # create an instance of the ResNet18 model with the weights from the ImageNet dataset
    # IMAGENET1K_V1 is a constant that contains a part of the enumeration of the weights available for the ResNet18 model, the weights found
    # to be the best for the model on the ImageNet dataset
    # set the model to evaluation mode, which means that the model will not change the weights during the evaluation, because
    # we don't want to train the model, just evaluate some images

    if not hasattr(obtain_photo_category_label, "preprocess"):
        obtain_photo_category_label.preprocess = transforms.Compose([
            transforms.Resize(256),  # Reduce longer side of the image to 256 pixels
            transforms.CenterCrop(224),  # Crop the center 224x224 pixels(ResNet18 expects 224x224 images)
            transforms.ToTensor(),  # Convert the image to a tensor: [1, 3, 224, 224]
            # Important: A tensor is a multidimensional matrix containing elements of a single data type, is the image represented as numbers
            # that the model can understand, first is the batch size(how many images processed at a time, then the number of channels(RGB),
            # then the height and width of the image
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            # Important: The ImageNet dataset was preprocessed with these values, so we need to use the same values,
            # because the model was trained on the ImageNet dataset, so it expects the input to be preprocessed in the same way
            # Normalization is important because it helps the model perform better and making fewer mistakes, without normalization
            # mistakes can happen even because of the contrast, brightness, etc. of the images
            # the mean and std have a value for each channel(RGB), the mean is the average value of the pixels in the image,
            # the std is the standard deviation of the pixels in the image, the values used here are specific to the ImageNet dataset
            # the formula used is: (input-mean)/std, which normalizes the image and makes it easier for the model to learn
        ])  # transforms.Compose is a class that allows us to chain multiple transformations together, in this case, we resize the image to 256x256 pixels
        # then we crop the image to 224x224 pixels, which is the size that the ResNet18 model expects, then we convert the image
        # to a tensor( a multi-dimensional matrix), which enables the model to process the image efficiently, and finally we normalize the image
        # so preprocess is a list of transformations that will be applied to the image


    img = Image.open(image_path).convert('RGB')  # Loads the image from the file path and converts it to RGB format
    img_tensor = obtain_photo_category_label.preprocess(img).unsqueeze(0).to(DEVICE)  # preprocess adds transformations to the image, then we add a dimension to the tensor
    # because we have only one image, but the model expects a batch of images, so we add a dimension to the tensor to make it a batch of one image

    # The gradient helps the model learn from the data, it is used to update the weights of the model during training, taking the shortest path
    # to the minimum error
    with torch.no_grad():  # disable gradient calculation, because we are not training the model, we are just using it to make predictions
        outputs = obtain_photo_category_label.model(img_tensor)  # output is the probability of each class, the model takes the image tensor as input and returns the output tensor
        # for resnet18 the output has 1000 classes, because it was trained on the ImageNet dataset, which has 1000 classes,
        # so 1000 possible classifications

    # outputs is a tensor for only one image, with 1000 probabilities, one for each class, the model outputs raw scores, which are not easy to interpret
    # we apply the softmax function on outputs[0] because we only have one image, so we take the first element of the tensor
    # dim will be 0, because we want to apply the softmax function to the first dimension of the tensor, so takes the class scores
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)  # apply the softmax function to the output tensor, which converts the output
    # to another tensor, but with the values between 0 and 1, and the sum of the values is 1, each representing a percentage of the probability
    # it is necessary because the model outputs raw scores, which are not easy to interpret, so we apply the softmax function to get probabilities
    # PS: softmax uses a complicated formula to calculate the probabilities, but the idea is that it gives a probability for each class
    #_, class_id = torch.max(probabilities, 0)  # class_id is the index of the class with the highest probability,
    prob, class_id = torch.topk(probabilities, top_n)  # get the top_n probabilities and their indices
    # the class that the model thinks the image belongs to
    # we don't care about the value of the highest probability, so we don't assign it to a variable, we use an underscore,
    # the function returns a tuple
    class_label = ResNet18_Weights.IMAGENET1K_V1.meta["categories"][class_id]  # takes the name of the class with the highest probability
    # .meta-> attribute contains metadata associated with the pre-trained weights, including the categories for classification
    return class_label