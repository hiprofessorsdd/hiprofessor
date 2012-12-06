cd /home/ubuntu/hiprofessor_git/hiprofessor/web_frontend
echo -e "\e[031mWARNING: This will overwrite contents of /var/www and /usr/lib/cgi-bin! Continue? [Y/n]"
read -e _Continue
echo -e "\e[037m"
if [ $_Continue != "Y" ]
then
  echo -e "Push to web cancelled"
  exit
fi

#check for swap files in either directory and further warn user:
_SwapForce=
_Directories=(/var/www /usr/lib/cgi-bin)
for directory in ${_Directories[*]}
do
  cd $directory
  for swap in *.swp
  do
    if [ "$swap" != "*.swp" ]
    then
      echo -e "\e[033mWARNING: $directory/$swap is present! Another user is likely editing text in there, and their work will be overwritten. Continue? [Y/n]"
      read -e _Continue
      echo -e "\e[037m"
      if [ $_Continue != "Y" ]
      then
        echo -e "Push to web cancelled!"
        exit
      else
        _SwapForce="*with swap forcing*"
      fi
    fi
  done
  for swap in .?*.swp
  do
    if [ "$swap" != ".?*.swp" ]
    then
      echo -e "\e[033mWARNING: $directory/$swap is present! Another user is likely editing text in there, and their work will be overwritten. Continue? [Y/n]"
      read -e _Continue
      echo -e "\e[037m"
      if [ $_Continue != "Y" ]
      then
        echo -e "Push to web cancelled!"
        exit
      else
        _SwapForce="*with swap forcing*"
      fi
    fi
  done
done

cd /home/ubuntu/hiprofessor_git/hiprofessor/web_frontend

echo -e "Enter your RCSID"
read -e _PusherRCSID
if [ -d PushLogs ];
then
  echo -e "\e[031m`date`\e[037m by $_PusherRCSID $_SwapForce" >> PushLogs/webPush.log
  echo -e "\e[031m`date`\e[037m by $_PusherRCSID $_SwapForce" >> PushLogs/wwwPush.log
  sudo cp -r www /var
  echo -e "\e[031m`date`\e[037m by $_PusherRCSID $_SwapForce" >> PushLogs/cgiPush.log
  sudo cp -r cgi-bin /usr/lib
fi
