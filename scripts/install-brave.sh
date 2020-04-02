#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# Check if Brave is installed
if [ $(sudo dpkg-query -W -f='${Status}' brave-browser 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Brave"

    cd ~
    curl https://s3-us-west-2.amazonaws.com/brave-apt-staging/keys.asc | sudo apt-key add -
    echo "deb [arch=amd64] https://s3-us-west-2.amazonaws.com/brave-apt-staging buster main" | sudo tee -a /etc/apt/sources.list.d/brave.list
    sudo apt update
    sudo apt install brave-keyring brave-browser
else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'brave-browser' already installed"
fi