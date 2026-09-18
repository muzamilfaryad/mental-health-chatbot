@echo off
echo Setting up Mental Health Chatbot...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Run the application
echo Starting chatbot application...
echo The chatbot will open in your browser automatically.
echo Press Ctrl+C to stop the server.
echo.
python app.py

pause
