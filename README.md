# Smart Image Sorter 🖼️

An AI-powered Python script that intelligently organizes images into thematic categories using object detection and image classification.

## Features

- **Advanced Categorization**  
  Automatically sorts images into 10+ categories:
  - 👤 Portrait (1 person)
  - 👫 Couple (2 people)
  - 👥 Group (3+ people)
  - 🌳 Nature (landscapes, plants, natural formations)
  - 🏙️ Urban (cityscapes, buildings, infrastructure)
  - 🍔 Food (dishes, ingredients, meals)
  - 🎨 Art (paintings, sculptures, artistic works)
  - 🚗 Vehicles (cars, bikes, transportation)
  - 🐾 Pets (domestic animals)
  - 📁 Non-Photos (non-image files)
  - 📦 Other (uncategorized images)

- **Dual AI Analysis**  
  Combines:
  - **RetinaNet**: Object detection for people counting
  - **ResNet18**: Image classification for thematic recognition

- **Customizable Categories**  
  Easily modify keywords and thresholds for different themes

## Installation

### Requirements
- Python 3.8+
- 4GB+ RAM (8GB recommended)
- 500MB+ disk space for AI models

### Setup Guide

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/Smart-Image-Sorter.git
   cd Smart-Image-Sorter
2. **Install Dependencies**
   ```bash
   pip install torch torchvision pillow imageai opencv-python
3. **Download AI Models**
   ```bash
   wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth -P models/
4. **Folder Sturcture**
   Smart-Image-Sorter/
├── models/
│   └── retinanet_resnet50_fpn_coco-eeacb38b.pth
├── test_photos/        # Your source folder
├── organize_photos.py  # Main script
└── README.md
## Usage
1. **Prepare Images**
   Place files in test_photos folder:
   test_photos/
├── family_reunion.jpg
├── sunset.jpg
├── steak_dinner.png
└── document.pdf
2. **Run the Sorter**
   ```bash
   python organize_photos.py
3. **View Organized Files**
    Results will appear in categorized subfolders:\
   test_photos/
├── Portrait/
├── Couple/
├── Group/
├── Nature/
├── Urban/
├── Food/
├── Art/
├── Vehicle/
├── Pet/
├── Non_Photos/
└── Other_Photos/
   
