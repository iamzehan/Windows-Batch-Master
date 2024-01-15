@echo off
setlocal enabledelayedexpansion

if "%1" == "" (
    echo Usage: %0 ^<project_name^>
    exit /b 1
)

set "ORIGINAL_DIR=%CD%"
set "ROOT_DIR=%1"

mkdir "%ROOT_DIR%" 2>nul
cd /D "%ROOT_DIR%" || exit /b 1

git init
echo.  > README.md
echo.  > LICENSE

mkdir data
cd data
mkdir raw processed annotations
cd ..

mkdir notebooks
cd notebooks
mkdir exploratory_data_analysis data_preprocessing model_development model_evaluation
cd ..

mkdir src
cd src
mkdir data_preprocessing model train evaluate utils
cd ..

mkdir config
cd config
echo.  > config.yaml
cd ..

mkdir tests
cd tests
mkdir unit_tests integration_tests
cd ..

mkdir results
cd results
mkdir model_weights evaluation_metrics figures logs
cd ..

mkdir models
cd models
mkdir pretrained_models
cd ..

mkdir outputs
cd outputs
mkdir predictions
cd ..

echo.  > requirements.txt

mkdir docs

echo.  > .gitignore

echo Object detection project directory structure created at %ROOT_DIR%
exit /b 0

