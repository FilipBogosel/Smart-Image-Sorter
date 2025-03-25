# Smart Image Sorter 🖼️
An AI-powered Python script that intelligently organizes images into thematic categories using object detection and image classification.
## 🌟 Key Features
- **Automatic Photo Organization**  
  `📂` Sorts images into 10+ intelligent categories:
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
- **AI-Powered Classification**  
  `🧠` Uses RetinaNet + ResNet18 models
- **Quick and easy Setup**  
  `⚡` Self-contained PowerShell installer
- **GPU Acceleration**  
  `🚀` Optional CUDA support for NVIDIA GPUs
- **Smart Error Handling**  
  `🛡️` Automatic recovery from processing errors
# To run the commands below youy should run Power Shell as an administrator
# Step 1
Clone this repository:
```bash
git clone https://github.com/FilipBogosel/Smart-Image-Sorter.git
```
# Step 2
Run the install.ps1 script
```bash
cd Smart-Image-Sorter
./install.ps1[GPU]
```
You should include the GPU only if you have a dedicated NVIDIA GPU and you want the AI in the project to be run by it(It requires quite large files to be installed)
# Step 3 
The program will be runed and you just have to input the path to the directory that contains the photos and wait.
# Step4: Enjoy!!!

# PS: I put a lot of comments in the code so anyone can understand it!!!
