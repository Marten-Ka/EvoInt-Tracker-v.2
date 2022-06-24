# EvoInt-Tracker-v.2

# Step 1:

- Download the Vikus-Viewer-Script from GitHub (https://github.com/cpietsch/vikus-viewer-script)
  - Extract into the main folder
  - Open the console in the "vikus-viewer-script"-folder
  - Type "npm install"

# Step 2:

## Step 2.1

- Check if you have installed a C++ compiler
  - Type "gcc" in a console
  - If the command exists, you can skip to Step 3

## Step 2.2

- Install a C++ compiler
- For example:
  - Install MinGW: https://sourceforge.net/projects/mingw/
    - Keep in mind: add bin folder to environment variables
  - Install Visual Studio (C++ compiler is included): https://visualstudio.microsoft.com/de/downloads/
- Make sure that the installation was successful by repeating Step 2.1

# Step 3:

## Step 3.1:

- Check if "CMake" is installed on your machine
  - Open a console and type "cmake --version"
  - If a version (e.g. "3.23.2") is printed, you can skip to Step 4

## Step 3.2:

- Install "CMake" through an installer or a zip (https://cmake.org/download/)
- Installer:
  - Download the latest ".msi" file
  - Execute the file and follow the setup
- ZIP:
  - Download the lastest ".zip" file
  - Extract it to a folder
  - Add the path to the folder to the PATH in the environment variables
- Make sure that the installation was successful by repeating Step 3.1

# Step 4:

## Step 4.1:

- Check if poppler is installed on your machine
  - Open a console and type "pdfinfo"
  - If there is valid output (e.g. version and help instructions), then you can skip to Step 5

## Step 4.2:

- Download the lastest release (should be a ".tar.xz" file) of poppler from: https://poppler.freedesktop.org/
- Unzip the file (e.g. with 7-Zip) in a folder (preferably: "C:\Program Files (x86)")
- Add the path to the "bin" folder inside the "Library" folder to the PATH environment variable
- Make sure that the installation was successful by repeating Step 3.1

# Step 5 (deprecated):

- Install Python-Poppler (https://cbrunet.net/python-poppler/installation.html)
- Run: "python setup.py install --install-lib C:/Users/dknecht/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages"

# Step 6:

- Open the console in the main folder
- Type "pip install -r requirements.txt" to download all dependencies
- Fix a bug in an dependency:
  - Go into the "prompt_toolkit"-folder in the "site-packages"-folder of your python installation folder
  - Navigate to the "styles"-folder and open the python file "from_dict.py"
  - Change line "from collections import Mapping" to "from collections.abc import Mapping"
  - Save and close the file
