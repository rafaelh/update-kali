#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\033[0m"

# === Exit without proceeding if proxychains is not installed ===
if [ ! -f /etc/proxychains.conf ]; then
    exit 0
fi

# Change Proxychains config from 9050 -> 8080
if grep -q "9050" /etc/proxychains.conf; then
  sudo sed -i 's/9050/8080/g' /etc/proxychains.conf
  echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating Proxychains to use port 8080"
fi