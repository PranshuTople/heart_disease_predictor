# Heart Disease Predictor

Dataset used: https://www.kaggle.com/ronitf/heart-disease-uci

### Step 1: Download Anaconda

If you are using Windows machine - https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe

OR

If you are using any other operating system - https://www.anaconda.com/products/individual

### Step 2: Download PyQt5

Open Anaconda Prompt and type the following commands
```
pip install pyqt5
```
```
pip install pyqt5-tools
```

### Step 3: Make GUI

Go into Anaconda's installed folder > Lib > site_packages > pyqt5_tools > Qt > bin > designer

Make GUI

Save it as .ui file

### Step 4: Convert it into python code

Open terminal in the location you saved the .ui file and run the following command
```
pyuic5 your_filename.ui -o your_filename.py -x
```

