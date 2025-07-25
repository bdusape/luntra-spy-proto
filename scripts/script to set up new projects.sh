#!/bin/bash

# Set up clean Python 3.11 virtual environment with FastAPI
echo "Creating clean Python 3.11 environment..."

# Make project dir if not already in one
mkdir -p fastapi-prototype && cd fastapi-prototype

# Remove old env if it exists
rm -rf venv

# Create new venv using Homebrew Python 3.11
python3 -m venv venv

# Activate env
source venv/bin/activate

# Upgrade pip + install packages
pip install --upgrade pip
pip install fastapi uvicorn jinja2

# Touch your app file
touch main.py

echo "✅ Environment ready. Run with: uvicorn main:app --reload"
