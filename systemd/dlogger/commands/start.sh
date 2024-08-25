#!/bin/bash

sudo cp systemd/dlogger/forge-dlogger.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable forge-dlogger
sudo systemctl start forge-dlogger