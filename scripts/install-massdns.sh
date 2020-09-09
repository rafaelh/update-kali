#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Check if MassDNS is installed
if [ ! -d "/opt/massdns" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing massdns"
    cd /opt
    sudo git clone https://github.com/blechschmidt/massdns
    cd /opt/massdns
    sudo make
    sudo ln -s /opt/massdns/bin/massdns /usr/local/bin/massdns
fi
