#! /bin/bash

# 1. Install Vim
echo "[INFO] Updating apt..."
sudo apt-get update 1>/dev/null
echo "[INFO] Installing vim..."
if ! vim --version &>/dev/null;then
  sudo apt-get install vim -y 1>/dev/null
else
  echo "[WARN] You have installed vim!"
fi

# 2. Config vim
echo "[INFO] Configurating vim..."
if [ ! -f /home/$USER/.vimrc ];then
  wget -q https://mr-addict.github.io/ghpages-fileserver/config/vim/vimrc -O /home/$USER/.vimrc
else
  echo "[WARN] You have already configurated vim in $USER!"
fi
if ! sudo test -f /root/.vimrc;then
  sudo cp /home/$USER/.vimrc /root
else
  echo "[WARN] You have already configurated vim in root!"
fi
echo "[INFO] Configuting vim as your default editor..."
sudo update-alternatives --set editor /usr/bin/vim.basic 1>/dev/null
