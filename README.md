[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/rafaelh/update-kali.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/rafaelh/update-kali/context:python) [![Twitter](https://img.shields.io/badge/twitter-@rafael_hart-blue.svg)](https://twitter.com/rafael_hart)

# update-kali
This is a tool to set up Kali Linux with additional packages and maintain them over time. You can also use this script with other debian-based distros like Ubuntu.

- [Usage](#Usage)
- [About](#About)
- [Config](#Config)
- [Optional Arguments](#Optional-arguments)
- [Using with Vagrant](#Using-with-vagrant)

![Image of update-kali script running](update-kali.gif)


# Usage

```
$ update-kali -h
usage: update-kali [-h] [-n] [-s] [-r] [-p] [-g] [-f]

update-kali is a tool for rapidly configuring Kali linux with additional packages, git repositories
and other tools, and maintaining them over time.

optional arguments:
  -h, --help        show this help message and exit
  -n, --noupdate    Don't check for an updated script
  -s, --noscripts   Don't run scripts
  -r, --noreposync  Don't sync git repos
  -p, --pip         Update all installed python pip packages
  -g, --gems        Update all installed ruby gem packages
  -f, --full        Do all optional updates
```

## About
I need to keep a group of Kali linux boxes up to date, and I like them to be setup in a similar format. This script installs the tools I'm likely to use, creates directories, etc. It's set up for my personal use, but with a little modification you can use it too:

* Fork the repo so that you can commit your changes to `config.py`, and so the script updates from your account fork in future
* Update `config.py` with your preferences
* Go through `/scripts/`, delete the ones you don't want, and add any of your own that you want to run.
* Make sure you have the following installed: `python3`, `python-apt` and `git`. These are all installed by default on the standard kali.

If you set up Kali VMs frequently, such as for different engagements, skip to the end of this document and consider using this script with [vagrant](https://www.vagrantup.com/).

## Config
The default config can be found in `config.py`. You should updated it to match what you want, otherwise you'll use my preferences and calamity will ensue. This script will:

* Perform a general package update
* Install and remove specified apt packages
* Install specified python modules, golang tools and ruby gems
* Set up and remove specified directories
* Sync specified git repos to `~/`, or a directory you nominate (private repos, such as dotfiles, notes, etc)
* Sync specified git repos to `/opt`, or a directory you nominate (public repos, such as wordlists)
* Run all the scripts in `/scripts`

**Note:** This script will change the ownership of your tools directory, which is `/opt` by default, to your user so that you aren't building with sudo privileges. Change the tools directory if you don't want that to happen.

## Optional Arguments

### Updating Go modules
The Go modules you install will most likely keep on getting worked on, but you'll only get the benefit of those once you update and recompile the associated repository. This can take a while, and introduces load, so Go modules will only be recompiled if the `-G` or `--rebuildgo` flags are used.

### Updating Python modules
If you run the tool with `-p` or `--pip`, it will update all python pip modules for your user. Be aware that this may introduce breaking changes for your Python scripts that aren't in [virtual environments](https://docs.python.org/3/library/venv.html).

### Updating Ruby Gems
As above, you can update all ruby gems with `-g` or `--gems`.

## Shell Scripts
Lastly, this tool will run each of the `.sh` or `.py` files in the `scripts` directory. If you add a script to this directory, make sure they can be run multiple times without causing a problem. You can use the following script that installs Google Chrome as a template:

``` sh
#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\033[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if Chrome is installed
if [ $(sudo dpkg-query -W -f='${Status}' google-chrome-stable 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing Google Chrome"
    cd ~
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    rm -rf google-chrome-stable_current_amd64.deb
fi
```

# Using with Vagrant
Another way this script can be useful is in concern with [Vagrant](https://www.vagrantup.com/), which will allow you to create a fresh kali vm, configured as you want with a simple `vagrant up`. Fresh kali box for every engagement? No problem.

1. Install [vagrant](https://www.vagrantup.com/)
2. Fork the repo so that you can commit your changes to `config.py`, and so the script updates from your account fork in future
3. Update `config.py` with your preferences
4. Go through `/scripts/`, delete the ones you don't want, and add any of your own that you want to run
5. Confirm that there aren't any changes you want to make to the `Vagrantfile`
6. Run `vagrant up`. Once the VM has finished provisioning and updating, you can ssh in using `vagrant ssh` or log in to Virtualbox/VMware with 'vagrant' as the username and password.

Does this mean [vagrant is insecure](https://stackoverflow.com/questions/14715678/vagrant-insecure-by-default/14719184)? Mostly no. `vagrant ssh` uses key authentication, which is generated on provisioning. **You do need to change the password though**