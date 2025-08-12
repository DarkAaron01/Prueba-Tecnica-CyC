@echo off
echo ====================================
echo  Sistema de Login - Litestar API
echo ====================================
echo.
echo Iniciando servidor...
echo.

REM Activar entorno virtual y ejecutar la aplicación
call .venv\Scripts\activate.bat
python app.py

echo.
echo Servidor detenido.
pause
