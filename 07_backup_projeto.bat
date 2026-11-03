@echo off

set DATA=%date:~6,4%-%date:~3,2%-%date:~0,2%
set HORA=%time:~0,2%-%time:~3,2%
set HORA=%HORA: =0%

set NOME=MarkdownConverter_%DATA%_%HORA%.zip

if not exist S:\MKD\Backups (
    mkdir S:\MKD\Backups
)

echo.
echo Criando backup...
echo.

powershell Compress-Archive ^
-Path ui,services,installer,*.py,*.txt,*.md,*.bat ^
-DestinationPath S:\MKD\Backups\%NOME% ^
-Force

echo.
echo Backup criado:
echo S:\MKD\Backups\%NOME%
echo.

pause