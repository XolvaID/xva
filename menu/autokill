#!/bin/bash
# ==========================================
# Color
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHT='\033[0;37m'
DF='\e[39m'
Bold='\e[1m'
Blink='\e[5m'
yell='\e[33m'
red='\e[31m'
green='\e[32m'
blue='\e[34m'
PURPLE='\e[35m'
cyan='\e[36m'
Lred='\e[91m'
Lgreen='\e[92m'
Lyellow='\e[93m'
NC='\e[0m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
LIGHT='\033[0;37m'
grenbo="\e[92;1m"
# ==========================================

clear
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"
Info="${Green_font_prefix}[ON]${Font_color_suffix}"
Error="${Red_font_prefix}[OFF]${Font_color_suffix}"
cek=$(grep -c -E "^# Autokill" /etc/cron.d/tendang)
if [[ "$cek" = "1" ]]; then
sts="${Info}"
else
sts="${Error}"
fi
clear
echo -e ""
echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
echo -e "            Status Autokill $sts           "
echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"
echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
echo -e "       1. AutoKill After 5 Minutes"
echo -e "       2. AutoKill After 10 Minutes"
echo -e "       3. AutoKill After 15 Minutes"
echo -e "       4. Turn Off AutoKill/MultiLogin"
echo -e "       5. Exit"
echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"                                                                                               
echo -e ""
read -p "Select From Options [1-4 or x] :  " AutoKill
echo -e ""
case $AutoKill in
                1)
                echo -e ""
                read -p "Multilogin Maximum Number Of Allowed: " max
                sleep 1
                clear
                echo > /etc/cron.d/tendang
                echo "# Autokill" >>/etc/cron.d/tendang
                echo "*/5 * * * *  root /usr/bin/tendang $max" >>/etc/cron.d/tendang
                echo -e ""
                echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
                echo -e ""
                echo -e "        Allowed MultiLogin : $max"
                echo -e "        AutoKill Every     : 5 Minutes"      
                echo -e ""
                echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"                                                                                                                                
                exit                                                                  
                ;;
                2)
                echo -e ""
                read -p "Multilogin Maximum Number Of Allowed: " max
                sleep 1
                clear
                echo > /etc/cron.d/tendang
                echo "# Autokill" >>/etc/cron.d/tendang
                echo "*/10 * * * *  root /usr/bin/tendang $max" >>/etc/cron.d/tendang
                echo -e ""
                echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
                echo -e ""
                echo -e "        Allowed MultiLogin : $max"
                echo -e "        AutoKill Every     : 10 Minutes"
                echo -e ""
                echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"
                exit
                ;;
                3)
                echo -e ""
                read -p "Multilogin Maximum Number Of Allowed: " max
                sleep 1
                clear
                echo > /etc/cron.d/tendang
                echo "# Autokill" >>/etc/cron.d/tendang
                echo "*/15 * * * *  root /usr/bin/tendang $max" >>/etc/cron.d/tendang
                echo -e ""
                echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
                echo -e ""
                echo -e "        Allowed MultiLogin : $max"
                echo -e "        AutoKill Every     : 15 Minutes"
                echo -e ""
                echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"
                exit
                ;;
                4)
                clear
                echo > /etc/cron.d/tendang
                echo -e ""
                echo -e "\033[1;93m┌──────────────────────────────────────────┐\033[0m"
                echo -e ""
                echo -e "        AutoKill MultiLogin Turned Off  "
                echo -e ""
                echo -e "\033[1;93m└──────────────────────────────────────────┘\033[0m"
                exit
                ;;
                x)
                clear
                exit
                ;;
        esac
