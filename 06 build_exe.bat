@echo off

echo ==========================================
echo Markdown Converter - Build EXE
echo ==========================================
echo.

call venv_build\Scripts\activate

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

pyinstaller ^
 --clean ^
 --noconfirm ^
 --onedir ^
 --windowed ^
 --collect-all markitdown ^
 --collect-all magika ^
 --add-data "S:\MKD\MarkdownConverter\venv_build\Lib\site-packages\magika\models;magika\models" ^
 main.py

echo.
echo Build concluido.
echo.

pause