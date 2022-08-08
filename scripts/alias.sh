#! /bin/bash

# Config alias
echo "[INFO] Configurating alias..."
if [ ! -f /home/$USER/.bash_aliases ];then
  wget -q https://mr-addict.github.io/ghpages-fileserver/config/alias/bash_aliases -O /home/$USER/.bash_aliases
else
  echo "[WARN] You have already configurate alias in $USER!"
fi
if ! sudo test -f /root/.bash_aliases;then
  sudo cp /home/$USER/.bash_aliases /root
else
  echo "[WARN] You have already configurate alias in root!"
fi
