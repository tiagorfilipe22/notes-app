@echo off
cd /d "%~dp0"
notes_app_env\Scripts\activate
python main.py
pause