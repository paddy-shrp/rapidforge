#!/bin/bash

SOURCE_DIR="config/nginx/sites"
AVAILABLE_DIR="/etc/nginx/sites-available/"
ENABLED_DIR="/etc/nginx/sites-enabled/"

cp "$SOURCE_DIR"* "$AVAILABLE_DIR"

for file in "$AVAILABLE_DIR"*; do
  filename=$(basename "$file")
  ln -sf "$AVAILABLE_DIR$filename" "$ENABLED_DIR$filename"
done

sudo nginx -t
sudo systemctl restart nginx




