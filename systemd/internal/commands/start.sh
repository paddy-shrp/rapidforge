#!/bin/bash

sudo cp systemd/internal/forge-internal.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable forge-internal
sudo systemctl start forge-internal