# This file defines what the update script should do. 

# Git Repositories
# My preference is to install most external repositories under a single directory in my home folder,
# and to the same with other people's repositories in a separate directory. These will be prefixed 
# with the user's home directory.
personal_repo_dir = '/x'
external_repo_dir = '/z'

# These directories will be removed from your home directory
directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

# These packages will be installed from APT. 
packages_to_install = ['most', 'ttf-mscorefonts-installer', 'pydf', 'htop', 'gobuster',
                       'exif', 'hexedit', 'python3-pip', 'python3-venv']

# These python packages will be installed globally
pip_packages = ['pipenv', 'pylint']

# These git repositories will be synced to the 'external repo' directory.
ext_repositories_to_sync = ['https://github.com/danielmiessler/SecLists',
                            'https://github.com/SecureAuthCorp/impacket',
                            'https://github.com/swisskyrepo/PayloadsAllTheThings',
                            'https://github.com/payloadbox/xss-payload-list']

# These git repositories will be synced to the 'personal repo' directory. '.git' will be stripped
# from each string.
personal_repositories_to_sync = ['git@github.com:rafaelh/security.git',
                                 'git@github.com:rafaelh/notes.git']

# Last of all, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
# provided it's # executable. For example, the current scripts install VS Code, Google Chrome and 
# Typora. Any script that goes in this directory should be written so it can run multiple times 
# without causing problems.
