@echo off

call %~dp0telegramBot\venv\Scipts\activate

cd %~dp0telegramBot

set TOKEN=5469111471:AAG0vgR754JQCMEjdGav2IyD2PNvfaRVJok

python bot_telegram.py

pause