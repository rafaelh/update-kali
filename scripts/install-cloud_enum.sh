#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if cloud_enum is installed
if [ ! -d "/opt/cloud_enum" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing cloud_enum"
    mkdir /opt/cloud_enum
    git clone https://github.com/initstring/cloud_enum /opt/cloud_enum
    pip3 install -r /opt/cloud_enum/requirements.txt
    sudo ln -s /opt/cloud_enum/cloud_enum.py /usr/local/bin/cloudenum
fi

# If it's already installed, check for updates
if [ -d "/opt/cloud_enum" ]
then
    cd /opt/cloud_enum
    git remote update 1>/dev/null
    HEADHASH=$(git rev-parse HEAD)
    UPSTREAMHASH=$(git rev-parse master@{upstream})
    if [ "$HEADHASH" != "$UPSTREAMHASH" ]; then
        # Actions to perform if there are remote updates
        echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating cloud_enum"
        git pull
    fi
    cd - 1>/dev/null
fi
