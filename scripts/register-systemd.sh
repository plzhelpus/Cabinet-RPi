#!/usr/bin/env bash
sudo cp cabinet.service /etc/systemd/system/cabinet.service
systemctl enable cabinet.service
systemctl start cabinet.service
