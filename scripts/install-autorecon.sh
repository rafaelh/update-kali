#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# === Exit without proceeding if run on a non-Kali distro ===
if ! grep -Fxvq "kali-rolling" /etc/debian_version; then
    exit 0
fi

# Check if autorecon is installed
if ! command -v autorecon &> /dev/null
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing Autorecon's dependencies"
    sudo apt install seclists curl dnsrecon enum4linux feroxbuster gobuster \
    impacket-scripts nbtscan nikto nmap onesixtyone oscanner redis-tools smbclient \
    smbmap snmp sslscan sipvicious tnscmd10g whatweb wkhtmltopdf
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing Autorecon"
    python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git
fi
