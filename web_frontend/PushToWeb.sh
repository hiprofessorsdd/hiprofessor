cd /home/ubuntu/hiprofessor_git/hiprofessor/web_frontend
echo -e "\e[031mWARNING: This will overwrite contents of /var/www and /usr/lib/cgi-bin! Continue? [Y/n]"
read -e _Continue
echo -e "\e[037m"
if [ $_Continue != "Y" ]
then
  echo -e "Push to web cancelled"
  exit
fi
echo -e "Enter your RCSID"
read -e _PusherRCSID
echo -e "\e[031m`date`\e[037m by $_PusherRCSID" >> PushLogs/webPush.log
echo -e "\e[031m`date`\e[037m by $_PusherRCSID" >> PushLogs/wwwPush.log
sudo cp -r www /var/www
echo -e "\e[031m`date`\e[037m by $_PusherRCSID" >> PushLogs/cgiPush.log
sudo cp -r cgi-bin /usr/lib/cgi-bin
