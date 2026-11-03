@echo off

set DATA=%date:~6,4%-%date:~3,2%-%date:~0,2%
set HORA=%time:~0,2%-%time:~3,2%
set HORA=%HORA: =0%

set DESTINO=S:\MKD\Backups\MarkdownConverter_v2.3.0_%DATA%_%HORA%.zip

powershell Compress-Archive ^
-Path ui,services,installer,*.py,*.md,*.txt,requirements.txt,.gitignore ^
-DestinationPath "%DESTINO%" ^
-Force

echo.
echo Backup concluido:
echo %DESTINO%
pause