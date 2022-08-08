# Step 1:

- Follow these steps for the two projects (sharpsheet, vikus-viewer-script):
  - Go into the folder
  - Open the console in the folder
  - Type "npm install"
  - If you are currently in the sharpsheet-folder, additionally type "npm run build"

# Step 2:

## Step 2.1

- Check if you have installed a C++ compiler
  - Type "gcc" in a console
  - If the command exists, you can skip to Step 3

## Step 2.2

- Install a C++ compiler
- For example:
  - Install MinGW: https://sourceforge.net/projects/mingw/
    - Mark "mingw32-gcc-g++" for installation
    - Click in top left corner on "Installation", then "Apply Changes"
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

- Download the lastest release (should be a ".7z" file) of poppler from: https://blog.alivate.com.au/poppler-windows/index.html
- Unzip the file (e.g. with 7-Zip on Windows) in a folder
- Add the path to the "bin" folder to the PATH environment variable
- Make sure that the installation was successful by repeating Step 4.1

# Step 5:

## Step 5.1:

- Check if python is installed
  - Open a console and type "python --version"
  - (The project was tested with Python 3.10, but may work with older versions)
  - If the command returned valid output, go to Step 5.2
  - If not, download python:
    - official: https://www.python.org/downloads/release/python-3100/
    - portable: https://sourceforge.net/projects/portable-python/

## Step 5.2:

- Check if pip is installed
- Type "pip --version"
- If the command failed, go to Step 5.3
- If the command returned valid output, go to Step 6

## Step 5.3:

- If python is installed, but pip not, follow the steps on this page: https://www.liquidweb.com/kb/install-pip-windows/

# Step 6:

- Open the console in the main folder
- Type "pip install -r requirements.txt" to download all dependencies
- Fix a bug in an dependency:
  - Go into the "prompt_toolkit"-folder in the "site-packages"-folder of your python installation folder
  - Navigate to the "styles"-folder and open the python file "from_dict.py"
  - Change line "from collections import Mapping" to "from collections.abc import Mapping"
  - Save and close the file

# Step 7:

- Open the console in the "evoint-scripts"-folder
- Type "python EvoInt.py" to run the CLI
- If there is an error with fitz, try:
  - python -m pip install --upgrade pymupdf (https://github.com/pymupdf/PyMuPDF/issues/1537)
