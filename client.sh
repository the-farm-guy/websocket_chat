#!/bin/bash

echo "Cloning the repository..."
git clone https://github.com/the-farm-guy/websocket_chat.git
cd websocket_chat || { echo "Failed to enter the repository directory."; exit 1; }

echo "Creating a Python virtual environment..."
python3 -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Updating pip..."
python3 -m pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirments.txt

echo "Navigating the directory"
cd group_chat || { echo "Failed to navigate to the group_chat directory."; exit 1; }

echo "Running the application"
python3 clients_server.py

echo "Script completed."
