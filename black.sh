#!/bin/bash

echo "🔹 Updating system..."
pkg update -y && pkg upgrade -y

echo "🔹 Installing Python..."
pkg install python -y

echo "🔹 Installing required Python libraries..."
pip install requests

echo "✅ All dependencies installed successfully!"

# 🔹 Black.py Ko Run Karna
echo "🚀 Running black.py..."
python black.py