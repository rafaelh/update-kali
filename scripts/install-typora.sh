#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -d /mnt/c/ ]; then exit 0; fi

# Check if typora is installed
if [ $(sudo dpkg-query -W -f='${Status}' typora 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Typora"

    # Add Typora's key and repository
    wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
    echo -e "\ndeb https://typora.io/linux ./" | sudo tee -a /etc/apt/sources.list
    sudo apt update

    # Install typora
    sudo apt install typora
else 
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'typora' already installed"
fi
