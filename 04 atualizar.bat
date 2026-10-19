@echo off

echo ========================================
echo Markdown Converter - Atualizacao
echo ========================================
echo.

call venv\Scripts\activate

echo Atualizando repositorio...
git pull

echo.
echo Atualizando dependencias...
python -m pip install -r requirements.txt --upgrade

echo.
echo Atualizacao concluida.
echo.

pause