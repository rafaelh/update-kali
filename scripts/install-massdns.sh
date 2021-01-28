#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if MassDNS is installed
if [ ! -d "/opt/massdns" ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing massdns"
    git clone https://github.com/blechschmidt/massdns /opt/massdns
    cd /opt/massdns
    make
    sudo ln -s /opt/massdns/bin/massdns /usr/local/bin/massdns
    cd - 1>/dev/null
fi

# If it's already installed, check for updates
if [ -d "/opt/massdns" ]
then
    cd /opt/massdns
    git remote update 1>/dev/null
    HEADHASH=$(git rev-parse HEAD)
    UPSTREAMHASH=$(git rev-parse master@{upstream})
    if [ "$HEADHASH" != "$UPSTREAMHASH" ]; then
        # Actions to perform if there are remote updates
        echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating massdns"
        git pull
        make
    fi
    cd - 1>/dev/null
fi

