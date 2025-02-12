# ===========CLASSIFICATION MODULE==========
import torch
from PIL import Image
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
from configuration import NATURE_KEYWORDS

def classify_nature(image_path):
    """Classify images using PyTorch's ResNet18."""
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.eval()

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    img = Image.open(image_path).convert('RGB')
    img_tensor = preprocess(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)

    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    _, class_id = torch.max(probabilities, 0)
    class_label = ResNet18_Weights.IMAGENET1K_V1.meta["categories"][class_id]

    return any(keyword in class_label.lower() for keyword in NATURE_KEYWORDS)