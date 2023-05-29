@echo off

call %~dp0telegramBot\venv\Scipts\activate

cd %~dp0telegramBot

set TOKEN=6198881058:AAEN_Dqd3bX82Mn0TLkqK4SAdpOgRKkjBnQ

python bot_telegram.py

pause