#! /bin/bash

# 1. Install git
echo "[INFO] Installing git..."
if ! command -v git &>/dev/null ;then
  sudo apt-get install git -y 1>/dev/null
else
  echo "[WARN] You have already installed git!"
fi

# 2. Config git
echo "[INFO] Configurating git..."
git config --global user.name MR-Addict
git config --global user.email 2750417853@qq.com
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
git config --global init.defaultBranch main
