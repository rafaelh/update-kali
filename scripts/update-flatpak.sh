#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if Flatpak is installed
if command -v flatpak 1>/dev/null 2>&1
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating Flatpak"
    sudo flatpak update -y
fi
