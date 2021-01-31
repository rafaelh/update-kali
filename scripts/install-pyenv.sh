#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# This script assumes the following settings are in .bashrc or .zshrc:
#
# export PYENV_ROOT="$HOME/.pyenv"
# export PATH="$PYENV_ROOT/bin:$PATH"
# if command -v pyenv 1>/dev/null 2>&1; then
#    eval "$(pyenv init -)"
# fi
#
# See https://www.kali.org/docs/general-use/using-eol-python-versions/


# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if autorecon is installed
if ! command -v pyenv 1>/dev/null 2>&1
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing pyenv's dependencies"
    sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
                        libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils \
                        tk-dev libffi-dev liblzma-dev python3-openssl git
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing pyenv"
    curl https://pyenv.run | bash
    pyenv install 2.7.18
fi
