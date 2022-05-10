# Jay Voice Assistant

#### For a cool demo of this project watch this 

It can do a lot of cool things, some of them being:
- Security Camera
- Motion Detection 
- Tell current time and date
- Open any website
- Tells about weather of any city
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Plays music
- Send email (with subject and content)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Tells a random joke
- Tells your IP address
- Can switch the window
- Can take screenshot and save it with custom filename
- Has a cool Graphical User Interface

## API Keys
To run this program you will require a bunch of API keys. Register your API key by clicking the following links

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframalpha](https://www.wolframalpha.com/)
  
## Installation

- First clone the repo
- Make a config.py file and include the following in it:
    ```weather_api_key = "<your_api_key>"
    email = "<your_email>"
    email_password = "<your_email_password>"
    wolframalpha_id = "<your_wolframalpha_id>"
- Copy the config.py file in Jarvis>config folder
- Make a new python environment
    If you are using anaconda just type ```conda create -n jarvis python==3.8.5 ``` in anaconda prompt
- To activate the environment ``` conda activate jarvis ```
- Navigate to the directory of your project
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` python main.py ```
- Enjoy !!!!

## Code Structure


    ├── driver
    ├── Jarvis              # Main folder for features 
    │   ├── config          # Contains all secret API Keys
    │   ├── features        # All functionalities of JARVIS 
    │   └── utils           # GUI images
    ├── __init__.py         # Definition of feature's functions
    ├── gui.ui              # GUI file (in .ui format)
    ├── main.py             # main driver program of Jarvis
    ├── requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  -  Make a new file in features folder, write the feature's function you want to include
  - Add the function's definition to __init__.py
  - Add the voice commands through which you want to invoke the function

## How to install Open cv
step 1 pip install opencv
## How to install FaceRecognitation

How to Install Face Recognition in Python on Windows?
Last Updated : 26 Oct, 2021
In this article, we will learn how to install Face Recognition in Python on Windows. Recognize and manipulate faces from Python or from the command line with the world’s simplest face recognition library. Built using dlib’s state-of-the-art face recognition built with deep learning.

Installing Face Recognition on Windows :
Prerequisites:
Face Recognition module can only be installed for Python version 3.7 and 3.8.

# Step 1: Install git for Windows

# Step 2: Clone this repository and go inside the folder using the following commands

# git clone https://github.com/RvTechiNNovate/face_recog_dlib_file.git
#   cd face_recog_dlib_file
#   git clone face_recog

#  Step 3: Enter the following command to install dlib and cmake using pip

Python 3.8:
pip install dlib-19.19.0-cp38-cp38-win_amd64.whl
pip install cmake
pip install dlib for python 3.8

Method 1: Using pip to install Face Recognition Package
Follow the below steps to install the Face Recognition package on Windows using pip:

Step 1: Install the latest Python3 in Windows 

Step 2: Check if pip and python are correctly installed.

python --version
pip --version
checking python and pip version in Windows 

Step 3: Upgrade your pip to avoid errors during installation.

pip install --upgrade pip
upgrading pip in Windows 

Step 4: Enter the following command to install Face Recognition using pip3.

pip install face-recognition


Method 2: Using setup.py to install Face Recognition 
Follow the below steps to install the Face Recognition on Windows using the setup.py file:

Step 1: Download the latest source package of Face Recognition for python3 from here.

curl https://files.pythonhosted.org/packages/6c/49/75dda409b94841f01cbbc34114c9b67ec618265084e4d12d37ab838f4fd3/face_recognition-1.3.0.tar.gz > face_recognition-1.3.0.tar.gz
downloading the source package for Face Recognition in Windows 

Step 2: Extract the downloaded package using the following command.

tar -xzvf face_recognition-1.3.0.tar.gz
extracting the face_recognition-1.3.0.tar.gz file in Windows 

Step 3: Go inside the folder and Enter the following command to install the package.

cd face_recognition-1.3.0
python setup.py install
installing Face Recognition on Windows using the setup.py file

Verifying Face Recognition installation on Windows :
Make the following import in your python terminal to verify if the installation has been done properly:

import face_recognition
Verifying Face Recognition installation on Windows 

If there is any error while importing the module then is not installed properly.