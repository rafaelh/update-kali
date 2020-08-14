#!/bin/bash
GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

if [ -d $HOME/.private ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo -n -e "Syncing .private: "
    git -C $HOME/.private pull
fi

if [ -d $HOME/dotfiles ]
then
    echo -ne $GREEN">>> "$ENDCOLOR; echo -n -e "Syncing dotfiles: "
    git -C $HOME/dotfiles pull
fi