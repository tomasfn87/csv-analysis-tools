#!/bin/bash

echo "1. Removing venv folder...";
rm -rf venv;

echo "2. Creating venv folder...";
python3 -m venv venv;

echo "3. Installing requirements.txt dependencies to venv...";
venv/bin/pip install --quiet --upgrade pip;
venv/bin/pip install --quiet --requirement requirements.txt;
