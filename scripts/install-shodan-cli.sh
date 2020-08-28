#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Install Shodan CLI, only if private repo with API key is synced ===

if [ -f ~/.private/apikeys/shodan ]; then
	shodan_key=`cat ~/.private/apikeys/shodan`

	# Check if Shodan is installed
	if ! `python3 -c "import shodan" 2>/dev/null`
	then 
		echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Shodan CLI"
		sudo easy_install shodan
		shodan init $shodan_key
	fi
fi
