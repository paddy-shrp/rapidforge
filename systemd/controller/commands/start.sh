#!/bin/bash

sudo cp systemd/controller/forge-controller.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable forge-controller
sudo systemctl start forge-controller