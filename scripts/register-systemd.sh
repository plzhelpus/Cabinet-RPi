#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo cp "${DIR}/cabinet.service" /etc/systemd/system/cabinet.service
sudo systemctl enable cabinet.service
sudo systemctl start cabinet.service
