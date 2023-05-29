@echo off

call %~dp0telegramBot\venv\Scipts\activate

cd %~dp0telegramBot

set TOKEN=#############################

python bot_telegram.py

pause