#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# Check if MassDNS is installed
if [ ! -d "/opt/massdns" ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing massdns"

    cd /opt
    sudo git clone https://github.com/blechschmidt/massdns
    cd /opt/massdns
    sudo make
    sudo ln -s /opt/massdns/bin/massdns /usr/local/bin/massdns

else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'massdns' already installed"
fi
