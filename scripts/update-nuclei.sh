#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

# Update nuclei templates if installed
if command -v nuclei &> /dev/null
then
    nuclei -update-templates
fi