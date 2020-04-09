#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# Update the Locate database
echo -ne $GREEN">>> "$ENDCOLOR; echo "Updating Locate database"
sudo updatedb

