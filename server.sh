#!/bin/bash

echo "Cloning the repository..."
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name || { echo "Failed to enter the repository directory."; exit 1; }

echo "Creating a Python virtual environment..."
python3 -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Navigating the directory"
cd group_chat || { echo "Failed to navigate to the group_chat directory."; exit 1; }

echo "Running the application"
python3 server_client.py

echo "Script completed."
