import os
import subprocess
import sys

''' This file defines what the update-kali script should do. '''

# Determine release, and whether we are on Windows Subsystem for Linux (WSL) so that we can set 
# different settings for different environments. Anything common can go outside the if statements.

release = subprocess.check_output("""sh -c '. /etc/os-release; echo "$NAME"'""", shell=True,
    universal_newlines=True).strip()
are_we_on_wsl = os.path.exists("/mnt/c/Windows/System32/wsl.exe")


if 'Kali' in release:
    # These directories will be removed from your home directory
    directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

    # These kali packages will be installed
    packages_to_install = ['most', 'ttf-mscorefonts-installer', 'pydf', 'htop', 'gobuster', 'amass',
                           'golang', 'exif', 'hexedit', 'jq', 'python3-pip', 'python3-venv',
                           'apt-transport-https', 'curl', 'filezilla', 'meld', 'ncat', 'net-tools',
                           'tmux', 'steghide', 'bash-completion', 'ieee-data', 'python3-netaddr',
                           'ruby-full', 'powercat', 'cewl', 'nbtscan', 'tree', 'upx-ucl',
                           'exe2hexbat', 'shellter', 'grc']

    # These kali packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint', 'dnsgen', 'stegcracker', 'truffleHog']

    # These gem packages will be installed globally
    gem_packages = ['wpscan']

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
                                'github.com/projectdiscovery/subfinder/cmd/subfinder',
                                'github.com/lc/gau',
                                'github.com/hakluke/hakrawler',
                                'github.com/hahwul/dalfox',
                                'github.com/ffuf/ffuf',
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                'https://github.com/swisskyrepo/PayloadsAllTheThings',
                                'https://github.com/payloadbox/xss-payload-list',
                                'https://github.com/Cillian-Collins/dirscraper',
                                'https://github.com/maurosoria/dirsearch',
                                'https://github.com/darkoperator/dnsrecon'
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    'git@github.com:rafaelh/dotfiles',
                                    'git@github.com:rafaelh/.private'
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

if 'Ubuntu' in release and not are_we_on_wsl:
    # These directories will be removed from your home directory
    directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

    # These Ubuntu packages will be installed
    packages_to_install = ['most', 'ttf-mscorefonts-installer', 'pydf', 'htop', 'golang', 'exif',
                           'hexedit', 'jq', 'python3-pip', 'python3-venv', 'apt-transport-https', 
                           'curl', 'filezilla', 'meld', 'ncat', 'net-tools', 'tmux', 
                           'bash-completion', 'ruby-full', 'nbtscan', 'tree', 'grc', 'john']

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint', 'stegcracker', 'truffleHog']

    # These gem packages will be installed globally
    gem_packages = ['wpscan']

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
                                'github.com/lc/gau',
                                'github.com/hakluke/hakrawler',
                                'github.com/hahwul/dalfox',
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    'git@github.com:rafaelh/dotfiles',
                                    'git@github.com:rafaelh/.private'
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

if 'Ubuntu' in release and are_we_on_wsl:
        # These directories will be removed from your home directory
    directories_to_remove = []

    # These Ubuntu packages will be installed
    packages_to_install = ['most', 'pydf', 'golang', 'exif', 'hexedit', 'jq', 'python3-pip',
                           'python3-venv', 'curl', 'net-tools', 'tmux', 'bash-completion',
                           'ruby-full', 'nbtscan', 'tree', 'grc']

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint']

    # These gem packages will be installed globally
    gem_packages = []

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    'git@github.com:rafaelh/dotfiles',
                                    'git@github.com:rafaelh/.private'
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.
