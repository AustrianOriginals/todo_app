@echo off
REM Quick Setup and Build Script for TODO App
REM This script installs dependencies and builds the Windows executable

setlocal enabledelayedexpansion

echo.
echo ========================================
echo TODO App - Windows Build Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip is not available
    echo Please reinstall Python with pip
    pause
    exit /b 1
)

echo [OK] pip found
echo.
echo Installing Python dependencies...
echo Please wait, this may take 1-2 minutes...
echo.

REM Install required packages
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed successfully
echo.
echo ========================================
echo Building Windows Executable...
echo ========================================
echo.

REM Remove old build artifacts
if exist build rmdir /s /q build >nul 2>&1
if exist dist rmdir /s /q dist >nul 2>&1

REM Create optimized executable
pyinstaller --onefile --windowed --name "TODO-App" --distpath dist --workpath build --specpath build --optimize 2 --strip --noupx --log-level ERROR src\main_advanced.py

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo [SUCCESS] Build completed!
    echo ========================================
    echo.
    echo Executable location:
    echo   dist\TODO-App.exe
    echo.
    echo File size: Check your dist folder
    echo Memory usage: ~80-150 MB at runtime
    echo.
    echo You can now run the executable standalone!
    echo.
    pause
) else (
    echo.
    echo [ERROR] Build failed
    echo Please check the error messages above
    echo.
    pause
    exit /b 1
)