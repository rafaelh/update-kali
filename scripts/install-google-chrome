#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# Check if Chrome is installed
if [ $(sudo dpkg-query -W -f='${Status}' google-chrome-stable 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Google Chrome"

    cd ~
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install google-chrome-stable_current_amd64.deb
    rm -rf google-chrome-stable_current_amd64.deb

else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'google-chrome-stable' already installed"
fi
