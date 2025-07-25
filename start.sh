#!/bin/bash
cd "$(dirname "$0")" || exit 1

if [ ! -f "venv/bin/activate" ]; then
  echo "❌ venv not found! Are you in the correct folder?"
  exit 1
fi

source venv/bin/activate
uvicorn main:app --reload
