#!/bin/bash
cd "$(dirname "$0")"/..
rm -rf venv
/usr/local/bin/python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
