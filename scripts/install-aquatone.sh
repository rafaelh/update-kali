#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# Check if aquatone is installed
if [ ! -f "/usr/local/bin/aquatone" ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing aquatone"

    cd /usr/local/bin
    sudo wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
    sudo unzip aquatone_linux_amd64_1.7.0.zip 
    sudo rm -rf README.md LICENSE.txt
else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'aquatone' already installed"
fi
