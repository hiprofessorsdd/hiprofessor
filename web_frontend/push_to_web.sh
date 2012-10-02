cd /home/ubuntu/hiprofessor_git/hiprofessor/web_frontend
echo -n -e "\e[031m`date`:\e[037m " >> cronlog.log
unison ./www/ /var/www/ 2>> cronlog.log
