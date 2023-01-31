#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\033[0m"

# === Exit without proceeding if ssh is not installed ===
if [ ! -f /etc/ssh/ssh_config ]; then
    exit 0
fi

# Allow old insecure algorithms
if ! grep -q "HostKeyAlgorithms" /etc/ssh/ssh_config; then
  sudo sh -c "echo \"    HostKeyAlgorithms +ssh-rsa,ssh-dss\" >> /etc/ssh/ssh_config"
  echo -ne $GREEN"[+] "$ENDCOLOR; echo "Updating ssh to accept connecting with insecure HostKeyAlgorithms"
fi