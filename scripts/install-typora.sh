#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if typora is installed
if [ $(sudo dpkg-query -W -f='${Status}' typora 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Typora"
    wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
    echo -e "\ndeb https://typora.io/linux ./" | sudo tee -a /etc/apt/sources.list
    sudo apt update
    sudo apt install typora
fi
