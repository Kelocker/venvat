@echo off

:: Update the version in pyproject.toml
python update_version.py

:: Clean previous builds
python clean.py

:: Build the package
python -m build
