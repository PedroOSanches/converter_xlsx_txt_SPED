@echo off
chcp 65001 >nul
call .venv/Scripts/Activate.bat
cd /d "%~dp0"
py main.py
echo.
pause