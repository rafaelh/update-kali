# update-kali
A script to set up Kali Linux with additional tools

## What is this?
I find that I need to keep a lot of Kali linux installations up to date, and I like them to be setup in a similar format. This script installs the tools I'm likely to use, creates directories, etc. Currently it's just set up for my personal use, but I'm intending to make it more generic over time.

## Config
The default config can be found in config.py. You should updated it to match what you want, otherwise you'll have my preferences used. This script will:

* Perform a general package update
* Install and remove specified packages
* Install specified python modules
* Install specified golang tools
* Set up some standardized directories

## Scripts
Lastly, this script will run each of the `.sh` or `.py` files in the `scripts` directory. If you add a script to this directory, make sure they can be run multiple times without causing a problem. You can use the following script that installs Google Chrome as a template:

``` sh
#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# Check if Chrome is installed
if [ $(sudo dpkg-query -W -f='${Status}' google-chrome-stable 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Google Chrome"

    cd ~
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i install google-chrome-stable_current_amd64.deb
    rm -rf google-chrome-stable_current_amd64.deb

else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'google-chrome-stable' already installed"
fi
```

