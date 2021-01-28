#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if dnsrecon is installed
if [ ! -d "/opt/dnsrecon" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing dnsrecon"
    git clone https://github.com/darkoperator/dnsrecon /opt/dnsrecon
    pip3 install -r /opt/dnsrecon/requirements.txt
    sudo ln -s /opt/dnsrecon/dnsrecon.py /usr/local/bin/dnsrecon
fi

# If it's already installed, check for updates
if [ -d "/opt/dnsrecon" ]
then
    cd /opt/dnsrecon
    git remote update 1>/dev/null
    HEADHASH=$(git rev-parse HEAD)
    UPSTREAMHASH=$(git rev-parse master@{upstream})
    if [ "$HEADHASH" != "$UPSTREAMHASH" ]; then
        # Actions to perform if there are remote updates
        echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating dnsrecon"
        git pull
        pip3 install -r /opt/dnsrecon/requirements.txt
    fi
    cd - 1>/dev/null
fi
