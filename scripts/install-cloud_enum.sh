#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Check if cloud_enum is installed
if [ ! -d "/opt/cloud_enum" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing cloud_enum"
    mkdir /opt/cloud_enum
    git clone https://github.com/initstring/cloud_enum /opt/cloud_enum
    sudo ln -s /opt/cloud_enum/cloud_enum.py /usr/local/bin/cloudenum
fi

# If it's already installed, check for updates
if [ -d "/opt/cloud_enum" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Checking for cloud_enum updates"
    cd /opt/cloud_enum
    git pull
    cd - 1>/dev/null
fi
