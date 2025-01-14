@echo off

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

:: Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Please install Pip and try again.
    pause
    exit /b
)

:: Install required libraries (tkinter is included with Python standard library)
pip install pillow tqdm opencv-python
if %errorlevel% neq 0 (
    echo Failed to install required libraries.
    pause
    exit /b
)

:: Run the Python script
python picstovideo.py
if %errorlevel% neq 0 (
    echo An error occurred while running the script.
    pause
    exit /b
)

pause
