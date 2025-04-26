echo "Navigating the directory"
cd group_chat || { echo "Failed to navigate to the group_chat directory."; exit 1; }

echo "Running the application"
python3 clients_server.py