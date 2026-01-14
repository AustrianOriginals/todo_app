@echo off
REM Fast rebuild - assumes dependencies already installed

echo Building TODO App...

REM Remove old build artifacts
if exist build rmdir /s /q build >nul 2>&1
if exist dist rmdir /s /q dist >nul 2>&1

REM Build executable
pyinstaller --onefile --windowed --name "TODO-App" --workpath build --specpath build --optimize 2 --strip --noupx src\main.py

if %errorlevel% equ 0 (
    echo Build successful! Executable: dist\TODO-App.exe
) else (
    echo Build failed
)
pause