#!/bin/bash

sudo cp systemd/example_service/rapidforge-example.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tapit-controller
sudo systemctl start tapit-controller