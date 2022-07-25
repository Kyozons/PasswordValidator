#!/usr/bin/env bash
DIST=$(lsb_release -a | awk '/Distributor ID:/{print $3}')

if [ $DIST = EndevourOS ] || [ $DIST = Garuda ]
then
    sudo pacman -S --noconfirm python-pip
    pip3 install requests bs4 pyperclip

elif [ $DIST = Ubuntu ] || [ $DIST = Regolith ]
then
    sudo apt install -y python-pip
    pip3 install requests bs4 pyperclip
fi
