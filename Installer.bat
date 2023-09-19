@echo off
REM Check if Python is installed
echo Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    cls
    echo Python is not installed. Please download it from the official website:
    echo https://www.python.org/downloads/windows/
) else (
    echo Installing all Packages...
    REM Install all packages
    python -m pip install disnake
    python -m pip install requests
    cls
    start
    echo All has been successfully installed.
    echo Now setup the config.json
    echo When you are ready press enter to start the bot
    start python /bot/main.py
)


REM Wait before closing the window
timeout /t 300