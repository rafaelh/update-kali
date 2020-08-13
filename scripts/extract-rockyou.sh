#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Check rockyou.txt.gz exists
if [ -f "/usr/share/wordlists/rockyou.txt.gz" ]
then
    # Check that it hasn't already been unzipped
    if [ ! -f "/usr/share/wordlists/rockyou.txt" ]
    then
        echo -ne $GREEN">>> "$ENDCOLOR; echo "Extracting rockyou.txt"
        sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
    fi
fi

