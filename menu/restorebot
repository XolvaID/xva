#!/bin/bash
red() { echo -e "\\033[32;1m${*}\\033[0m"; }
IP=$(curl -s ipv4.icanhazip.com)
HOST="$(cat /etc/xray/domain)"
DATEVPS=$(date +"%d-%B-%Y")
ISPVPS=$(cat /etc/xray/isp)
CITY=$(cat /etc/xray/city)
GREEN="\e[92;1m"
BLUE="\033[36m"
RED='\033[0;31m'
NC='\033[0m'
function RESTOREVPS() {
    unzip *.zip >/dev/null 2>&1
    #    rm -f *.zip >/dev/null 2>&1
    cp /etc/adminbot/backup/passwd /etc/
    cp /etc/adminbot/backup/group /etc/
    cp /etc/adminbot/backup/shadow /etc/
    cp /etc/adminbot/backup/gshadow /etc/
    cp -r /etc/adminbot/backup/html /var/www/
    cp -r /etc/adminbot/backup/ssh /etc/
    cp -r /etc/adminbot/backup/vmess /etc/
    cp -r /etc/adminbot/backup/vless /etc/
    cp -r /etc/adminbot/backup/trojan /etc/
    cp -r /etc/adminbot/backup/limit /etc/
    cp -r /etc/adminbot/backup/shadowsocks /etc/
    cp -r /etc/adminbot/backup/*.json /etc/xray >/dev/null 2>&1
    cp -r /etc/adminbot/backup/*.log /etc/xray >/dev/null 2>&1
    cp /etc/openvpn/*.ovpn /var/www/html/
    cd
    systemctl restart xray >/dev/null 2>&1
    rm -f /etc/adminbot/*.zip >/dev/null 2>&1
    rm -rf /etc/adminbot/backup >/dev/null 2>&1
    echo -e "◇━━━━━━━━━━━━━━━━━━━━━━━━━◇"
    echo -e "SUCCESSFULL RESTORE YOUR VPS"
    echo -e "Please Save The Following Data"
    echo -e "◇━━━━━━━━━━━━━━━━━━━━━━━━━◇"
    echo -e "Your VPS IP : $IP"
    echo -e "DOMAIN      : $HOST"
    echo -e "DATE        : $DATEVPS"
    echo -e "ISP         : $ISPVPS"
    echo -e "LOCATION    : $CITY"
    echo -e "◇━━━━━━━━━━━━━━━━━━━━━━━━━◇"
    echo -e "Dont Forget Renew Your SSL CRT"
    echo -e "Please Reboot Vps"
}
cd /etc/adminbot
RESTOREVPS
