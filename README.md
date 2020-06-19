# update-kali
Scripts to set up Kali Linux with additional tools, and maintain them.

## What is this?
I find that I need to keep a lot of Kali linux installations up to date, and I like them to be setup in a similar format. This script installs the tools I'm likely to use, creates directories, etc. Currently it's just set up for my personal use, but I'm intending to make it more generic over time.

## Config
The default config can be found in config.py. You should updated it to match what you want, otherwise you'll have my preferences used. This script will:

* Perform a general package update
* Install and remove specified packages
* Install specified python modules
* Install specified golang tools
* Set up some standardized directories

**Note:** The script will change the ownership of your tools directory, which is `/opt` by default, to your user so that you aren't building with sudo privileges. Change the tools directory if you don't want that to happen.

## Updating Go modules
The Go modules you install will most likely keep on getting worked on, but you'll only get the benefit of those once you update and recompile the associated repository. This takes a long time, so I've added a separate command `update-go-modules` that iterates through updating them.

## Updating Python modules
You can update all python pip modules across the system using `update-python-modules`. Be aware that this may introduce breaking changes for your Python scripts, which is why venv is your friend.

## Scripts
Lastly, this script will run each of the `.sh` or `.py` files in the `scripts` directory. If you add a script to this directory, make sure they can be run multiple times without causing a problem. You can use the following script that installs Google Chrome as a template:

``` sh
#!/bin/bash
GREEN="\033[1;32m"
GREY="\033[0;37m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -d /mnt/c/ ]; then
    echo -ne $GREY">>> "$ENDCOLOR; echo "Skipping Google Chrome on WSL"
    exit 0
fi

# Check if Chrome is installed
if [ $(sudo dpkg-query -W -f='${Status}' google-chrome-stable 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo "Installing Google Chrome"

    cd ~
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    rm -rf google-chrome-stable_current_amd64.deb

else
    echo -ne $GREY">>> "$ENDCOLOR; echo "Package 'google-chrome-stable' already installed"
fi
```

