#! /bin/bash

# 1. Install omp
echo "[INFO] Installing oh-my-posh..."
if ! command -v oh-my-posh &>/dev/null ;then
  sudo wget -q https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
  sudo chmod +x /usr/local/bin/oh-my-posh
else
  echo "[WARN] You have already installed oh-my-posh!"
fi

# 2. Istall hack fonts
echo "[INFO] Installing hack fonts..."
sudo apt-get -y install fonts-hack-ttf 1>/dev/null

# 3. Install themes
echo "[INFO] Installing oh-my-posh themes..."
if [ ! -d /home/$USER/.poshthemes ];then
  mkdir /home/$USER/.poshthemes
  wget -q https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O /home/$USER/.poshthemes/themes.zip
  unzip -q -o /home/$USER/.poshthemes/themes.zip -d /home/$USER/.poshthemes
  chmod u+rw /home/$USER/.poshthemes/*.omp.*
  rm /home/$USER/.poshthemes/themes.zip
else
  echo "[WARN] You have already installed oh-my-posh themes!"
fi

# 4. Config bash
echo "[INFO] Configurating oh-my-posh for bash..."
if ! grep -q oh-my-posh /home/$USER/.bashrc ;then
  sed -i "$ a\eval \"\$(oh-my-posh --init --shell bash --config /home/$USER/.poshthemes/paradox.omp.json)\"" /home/$USER/.bashrc
else
  echo "[WARN] You have already configurated oh-my-posh for $USER!"
fi
if ! sudo grep -q oh-my-posh /root/.bashrc ;then
  sudo sed -i "$ a\eval \"\$(oh-my-posh --init --shell bash --config /home/$USER/.poshthemes/paradox.omp.json)\"" /root/.bashrc
else
  echo "[WARN] You have already configurated oh-my-posh for root!"
fi
