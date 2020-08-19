#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Check if unzip is installed, to be able to install aquatone
if [ $(sudo dpkg-query -W -f='${Status}' unzip 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Unzip"
    sudo apt install -y unzip
fi

# Check if aquatone is installed
if [ ! -f "/usr/local/bin/aquatone" ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing aquatone"

    cd /usr/local/bin
    sudo wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
    sudo unzip aquatone_linux_amd64_1.7.0.zip
    sudo rm -f README.md LICENSE.txt aquatone_linux_amd64_1.7.0.zip
fi
