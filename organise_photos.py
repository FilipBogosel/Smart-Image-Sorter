import os# os module provides a way of using operating system functionalities
import shutil# shutil module provides some functions to work with file objects and directories
import torch# PyTorch is an open source machine learning library from which we will use the ResNet18 model
from PIL import Image# PIL is the Python Imaging Library, which we will use to load images
# torchvision is a package in PyTorch that contains popular datasets, model architectures,
# and common image transformations for computer vision
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights# import the ResNet18 model and its weights
#Important: An AI model's weights are the values that the model is using to make predictions,
# they are like arguments to a function. The weights are learned during the training of the model.
# Those weights are like the characteristics of the things that the model is trying to predict.
from imageai.Detection import ObjectDetection# import the ObjectDetection class from the imageai.Detection module

# ========== CONFIGURATION ========== #
SOURCE_FOLDER = "D:\\Github\\Smart-Image-Sorter\\test_photos"
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
DESTINATION_FOLDERS = {
    'portrait': "Portrait",# portrait = 1 person
    'couple': "Couple",# couple = 2 people
    'group': "Group",# group = 3+ people
    'nature': "Nature",# nature = nature photos, but not with people
    'urban': "Urban",# urban = cityscape, buildings, etc.
    'food': "Food",# food = food photos
    'art': "Art",# art = paintings, sculptures, etc.
    'vehicle': "Vehicle",# vehicle = cars, bikes, etc.
    'pet': "Pet",# pet = photo with animals, but not in nature, so if it does not find any keyword in the nature
    # category, but it finds a keyword for an animal, it will be classified as a pet
    'non_photos': "Non_Photos",# non_photos = non-image files
    'other': "Other_Photos"# other = images that don't fit the above categories
}

NATURE_KEYWORDS = {
    'tree', 'flower', 'mountain', 'forest', 'river', 'valley', 'field', 'lake',
    'ocean', 'sky', 'cloud', 'sunset', 'waterfall', 'leaf', 'plant', 'grass','bush','cactus',
    'desert','beach','sand','rock','cave','volcano','island','jungle','rainforest','savanna',
    'tundra','arctic','antarctic','glacier','wetland','marsh','swamp','mangrove','reef','coral',
    'sea','seashore','shore','coast','cliff','canyon','hill','valley','plateau','mesa'
}#keywords that can be found in nature photos when they are analyzed by the ResNet18 model

URBAN_KEYWORDS = {
    'city', 'town', 'village', 'street', 'road', 'building', 'house', 'apartment', 'skyscraper',
    'office', 'store', 'shop', 'restaurant', 'cafe', 'hotel', 'motel', 'parking', 'station',
    'airport', 'harbor', 'port', 'bridge', 'tunnel', 'plaza', 'square', 'market', 'mall', 'cinema',
    'theater', 'museum', 'library', 'school', 'college', 'university', 'hospital', 'clinic', 'police',
    'fire', 'post', 'office', 'bank', 'church', 'temple', 'mosque', 'synagogue', 'stadium',
    'arena', 'court', 'field', 'park', 'garden', 'zoo', 'aquarium', 'amusement', 'playground','fountain'
}#keywords that can be found in urban photos when they are analyzed by the ResNet18 model


# ========== HELPER FUNCTIONS ========== #
def initialize_folders():
    """Create destination folders."""
    for folder in DESTINATION_FOLDERS.values():
        folder_path = os.path.join(SOURCE_FOLDER, folder)
        os.makedirs(folder_path, exist_ok=True)
    print("Folders created!")


def setup_detector():
    """Initialize the people detector (RetinaNet)."""
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join("models", "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
    detector.loadModel()
    print("Detection model loaded!")
    return detector


def classify_nature(image_path):
    """Classify images using PyTorch's ResNet18."""
    # Load the model
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.eval()  # Set to evaluation mode

    # Preprocess the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    img = Image.open(image_path).convert('RGB')
    img_tensor = preprocess(img).unsqueeze(0)

    # Make predictions
    with torch.no_grad():
        outputs = model(img_tensor)

    # Decode predictions
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    _, class_id = torch.max(probabilities, 0)
    class_label = ResNet18_Weights.IMAGENET1K_V1.meta["categories"][class_id]

    return any(keyword in class_label.lower() for keyword in NATURE_KEYWORDS)


def process_image(file_path, detector):
    """Categorize the image."""
    try:
        # Detect people
        detections = detector.detectObjectsFromImage(
            input_image=file_path,
            output_image_path=None,
            minimum_percentage_probability=40
        )
        person_count = sum(1 for obj in detections if obj["name"] == "person")

        # Determine category
        if person_count == 2:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['couple'])
        elif person_count > 2:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['group'])
        else:
            return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['nature']) \
                if classify_nature(file_path) \
                else os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['other'])
    except Exception as e:
        print(f"Error processing image: {e}")
        return os.path.join(SOURCE_FOLDER, DESTINATION_FOLDERS['other'])


# ========== MAIN FUNCTION ========== #
def organize_photos():
    initialize_folders()
    detector = setup_detector()

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