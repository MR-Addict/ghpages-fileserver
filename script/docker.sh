#! /bin/bash

# 1. Install docker
echo "[INFO] Installing docker..."
if ! command -v docker &>/dev/null ;then
  sudo apt-get install docker.io -y 1>/dev/null
  sudo usermod -aG docker $USER
else
  echo "[WARN] You have already installed docker!"
fi

# 2. Config daemon.json for docker
if ! sudo test -f /etc/docker/daemon.json ;then
  sudo wget -q https://mraddict.one/ghpages-fileserver/config/docker/daemon.json -O /etc/docker/daemon.json
else
  echo "[WARN] You have configurated daemon.json!"
fi

# 3. Install docker-compose
echo "[INFO] Installing docker-compose"
if ! command -v docker-compose &>/dev/null ;then
  wget -q https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -O docker-compose
  chmod +x docker-compose
  sudo mv docker-compose /usr/local/bin
else
  echo "[WARN] You have installed docker-compose"
fi
