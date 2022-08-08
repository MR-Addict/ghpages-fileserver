#! /bin/bash

# 1. Install mdbook
echo "[INFO] Installing mdbook..."
if ! command -v mdbook &>/dev/null ;then
  wget -q https://github.com/rust-lang/mdBook/releases/download/v0.4.18/mdbook-v0.4.18-x86_64-unknown-linux-gnu.tar.gz -O mdbook.tar.gz
  tar -zxf mdbook.tar.gz
  rm mdbook.tar.gz
  chmod u+x mdbook
  sudo mv mdbook /usr/local/bin
else
  echo "[WARN] You have already installed mdbook!"
fi
echo "[INFO] Installing mdbook-admonish..."

# 2. Install mdbook-admonish
if ! command -v mdbook-admonish &>/dev/null ;then
  wget -q https://github.com/tommilligan/mdbook-admonish/releases/download/v1.7.0/mdbook-admonish-v1.7.0-x86_64-unknown-linux-gnu.tar.gz -O mdbook-admonish.tar.gz
  tar -zxf mdbook-admonish.tar.gz
  rm mdbook-admonish.tar.gz
  chmod u+x mdbook-admonish
  sudo mv mdbook-admonish /usr/local/bin
else
  echo "[WARN] You have already installed mdbook-admonish!"
fi
