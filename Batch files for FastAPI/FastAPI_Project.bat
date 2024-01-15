@echo off
if "%1" == "" (
    echo Usage: %0 ^<project_name^>
    exit /b 1
)
set "ORIGINAL_DIR=%CD%"
set "ROOT_DIR=%1"

mkdir "%ROOT_DIR%" 2>nul
cd /D "%ROOT_DIR%" || exit /b 1

mkdir app
cd app || exit /b 1
echo. > __init__.py
echo. > main.py

mkdir auth
cd auth || exit /b 1
echo. > __init__.py
echo. > auth_handler.py
echo. > token_model.py
echo. > user.py
cd ..

mkdir server
cd server || exit /b 1
echo. > __init__.py
echo. > app.py
echo. > database.py

mkdir models
mkdir routes

cd ..

echo. > requirements.txt

cd /D "%ORIGINAL_DIR%"
echo Project directory structure created at %ROOT_DIR%.
