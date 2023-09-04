#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

YELLOW="\033[1;33m"
ENDCOLOR="\e[0m"

# Update nuclei templates if installed
if command -v creds &> /dev/null
then
    echo -ne $YELLOW"[>] "$ENDCOLOR; echo "Updating Default Credentials tool (creds)"
    creds update
fi
