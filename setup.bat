@echo off
setlocal enabledelayedexpansion

echo [92m=== Jarvis AI Assistant Setup (Anaconda) ===[0m

:: Set Anaconda paths
set ANACONDA_PATH=%UserProfile%\anaconda3
set CONDA_CMD=%ANACONDA_PATH%\Scripts\conda.exe

:: Check Conda installation
if not exist "%CONDA_CMD%" (
    echo [91mError: Anaconda not found in %ANACONDA_PATH%[0m
    echo Please make sure Anaconda is installed in the default location
    pause
    exit /b 1
)

:: Create or activate conda environment
if exist %ANACONDA_PATH%\envs\jarvis (
    echo [93mFound existing conda environment 'jarvis'[0m
    choice /C YN /M "Do you want to create a fresh environment"
    if errorlevel 2 goto ACTIVATE
    "%CONDA_CMD%" env remove -n jarvis
)

:CREATE
echo [92mCreating conda environment...[0m
"%CONDA_CMD%" create -n jarvis python=3.9 -y
if errorlevel 1 (
    echo [91mFailed to create conda environment[0m
    pause
    exit /b 1
)

:ACTIVATE
echo [92mActivating conda environment...[0m
call %ANACONDA_PATH%\Scripts\activate.bat jarvis

:: Install dependencies
echo [92mInstalling dependencies...[0m
pip install -r requirements.txt

:: Create necessary directories and files
echo [92mCreating project structure...[0m
if not exist DataBase mkdir DataBase
if not exist Data mkdir Data
type nul > DataBase\chat_log.txt
type nul > DataBase\qna_log.txt

:: Configure API key
if not exist .env (
    echo [93mSetting up OpenAI API key...[0m
    set /p API_KEY="Enter your OpenAI API key: "
    echo OPENAI_API_KEY=!API_KEY!> .env
)

echo [92m=== Setup Complete! ===[0m
echo.
echo To start the application, run:
echo [96mcall %ANACONDA_PATH%\Scripts\activate.bat jarvis[0m
echo [96mstreamlit run streamlit_app.py[0m
echo.
pause
