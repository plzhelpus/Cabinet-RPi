#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo cp "${DIR}/cabinet.service" /etc/systemd/system/cabinet.service
systemctl enable cabinet.service
systemctl start cabinet.service
