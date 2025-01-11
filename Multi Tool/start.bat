@echo off
color 1



    echo Do you have Python 3.12 or above installed? (enter "y" for yes or "n" for no) 
    choice /c yn /n /m "Your choice: "

    if errorlevel 2 (
        color 4
        echo Please install Python 3.12 or above for this app to work properly.
        echo Open this file again once you have installed latest version of python. 
        start https://www.python.org/
        pause
        exit /b 1
    )
)
color 2
echo Installing Python dependencies...
python -m pip install -r requirements.txt
start main.py






