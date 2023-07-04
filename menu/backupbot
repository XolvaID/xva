#!/bin/bash
# // font
red() { echo -e "\\033[32;1m${*}\\033[0m"; }
IP=$(curl -s ipv4.icanhazip.com)
HOST="$(cat /etc/xray/domain)"
DATEVPS=$(date +"%d-%B-%Y")
ISPVPS=$(cat /etc/xray/isp)
TIME=10
CITY=$(cat /etc/xray/city)
GREEN="\e[92;1m"
BLUE="\033[36m"
RED='\033[0;31m'
NC='\033[0m'
#bottoket
source /etc/adminbot/var.txt
URL=https://api.telegram.org/bot$BOT_TOKEN/sendDocument
HOST="$(cat /etc/xray/domain)"
function BACKUPVPS() {
    mkdir -p /root/backup
    cp -r /etc/xray/config.json backup/ >/dev/null 2>&1
    cp -r /etc/xray/*.log backup/ >/dev/null 2>&1
    cp /etc/passwd backup/
    cp /etc/group backup/
    cp /etc/shadow backup/
    cp /etc/gshadow backup/
    cp -r /var/www/html backup/html
    cp -r /etc/ssh backup/
    cp -r /etc/vmess backup/
    cp -r /etc/vless backup/
    cp -r /etc/limit backup/
    cp -r /etc/trojan backup/
    cp -r /etc/shadowsocks/ backup
    zip -r ${DATEVPS}.zip backup >/dev/null 2>&1
    
cd /root
curl -F chat_id="$ADMIN" -F document=@"${DATEVPS}.zip" -F caption="$HOST " $URL >/dev/null 2>&1

rm -f ${DATEVPS}.zip
rm -rf backup
}
cd /root
BACKUPVPS
