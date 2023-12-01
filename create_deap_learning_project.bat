@echo off
if "%1" == "" (
    echo Usage: %0 ^<project_name^>
    exit /b 1
)
set "ORIGINAL_DIR=%CD%"
set "ROOT_DIR=%1"

mkdir "%ROOT_DIR%" 2>nul
cd /D "%ROOT_DIR%" || exit /b 1

git init .
mkdir data
mkdir data\raw data\processed data\external
mkdir notebooks
mkdir notebooks\eda notebooks\model_development notebooks\evaluation
mkdir src
mkdir src\data_preprocessing src\model src\train src\evaluate src\utils
mkdir config
echo.  > config\config.yaml
mkdir tests
mkdir tests\unit_tests tests\integration_tests
mkdir results
mkdir results\model_weights results\figures results\logs
mkdir experiments
mkdir models
mkdir models\pretrained_models
mkdir outputs
mkdir outputs\predictions
echo.  > requirements.txt
mkdir docs
echo.  > .gitignore
echo. > README.md 

echo Project directory structure created at %ROOT_DIR%.

cd /D "%ORIGINAL_DIR%"



 

