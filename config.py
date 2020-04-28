import os

# This file defines what the update script should do.

# Git Repositories
# My preference is to install most external repositories, Go tools, etc under /opt, and to keep all
# my git repositories in a single directory under my home folder.
home_dir = os.getenv("HOME")

personal_repo_directory = home_dir + '/x'
external_tools_directory = '/opt'

# These directories will be removed from your home directory
directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

# These kali packages will be installed
packages_to_install = ['most', 'ttf-mscorefonts-installer', 'pydf', 'htop', 'gobuster', 'amass',
                       'golang', 'exif', 'hexedit', 'jq', 'python3-pip', 'python3-venv',
                       'apt-transport-https', 'curl', 'ufw', 'gufw', 'filezilla', 'meld']

# These kali packages will be removed
packages_to_remove = ['chromium']

# These python packages will be installed globally
pip_packages = ['pipenv', 'pylint', 'dnsgen']

# These go tools will be installed globally. You will need to have the following settings in your
# .bashrc already:
#
# export GOROOT=/usr/lib/go
# export GOPATH=$HOME/go
# export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
golang_modules_to_install = ['github.com/tomnomnom/assetfinder',
                             'github.com/projectdiscovery/subfinder/cmd/subfinder',
                             'github.com/lc/gau',
                             'github.com/theblackturtle/wildcheck',
                             'github.com/tomnomnom/httprobe',
                             'github.com/hakluke/hakrawler',
                             'github.com/tomnomnom/qsreplace']

# These git repositories will be synced to the 'external repo' directory
ext_repositories_to_sync = ['https://github.com/danielmiessler/SecLists',
                            'https://github.com/SecureAuthCorp/impacket',
                            'https://github.com/swisskyrepo/PayloadsAllTheThings',
                            'https://github.com/payloadbox/xss-payload-list',
                            'https://github.com/Cillian-Collins/dirscraper',
                            'https://github.com/maurosoria/dirsearch']

# These git repositories will be synced to the 'personal repo' directory. '.git' will be stripped
# from each string.
personal_repositories_to_sync = ['git@github.com:rafaelh/security.git',
                                 'git@github.com:rafaelh/notes.git']

# Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
# provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
# Typora. Any script that goes in this directory should be written so it can run multiple times
# without causing problems.

# Services to print the status of. I use different services on different installations, so it's
# useful to be reminded of what is started.
systemd_services = ['sshd', 'postgresql', 'ufw']
