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
# To run the commands below youy should run Power Shell as an administrator,
# press windows key, tyme PowerShell, right click on it and select run as administrator and use the following comand to go to the folder where you want to install the program at(you can copy the path from file explorer, top part, click on it then copy and paste after cd):
```bash
cd folder_path
```
# Step 1
Clone this repository(copy paste this comand in PowerShell and press Enter):
```bash
git clone https://github.com/FilipBogosel/Smart-Image-Sorter.git
```
After you clone the repository, run the following command to enable running the install.ps1 file:
```
powershell -noexit -ExecutionPolicy Bypass -File install.ps1
```
# Step 2
Run the install.ps1 script:
```bash
cd Smart-Image-Sorter
./install.ps1
```
Or, if you want to use your GPU:
```bash
cd Smart-Image-Sorter
./install.ps1 GPU
```
You should include the GPU only if you have a dedicated NVIDIA GPU and you want the AI in the project to be run by it(It requires quite large files to be installed)
# Step 3 
The program will be runed and you just have to input the path to the directory that contains the photos and wait.
# Step 4: 
If you want to run the program after the install run it using the commands wherever you open PowerShell(filepath denotes the path were you downloaded the repository with the .py files):
```bash
cd filepath\Smart-Image-Sorter\src
python organise_photos.py
```
Replace path according to your case
EX: filepath = D:\App, the command will be cd D:\App\Smart-Image-Sorter\src
# Step 5: Enjoy!!!

# PS: I put a lot of comments in the code so anyone can understand it!!!
