#/bin/bash/!

# written by Tim Treese (RCSID treest)
# 9.14.2012 for SSD project hiprofessor

if [ "$1" ]; then
  if [ "$1" == "fall" ]; then
    SCHED_PULL_SEMESTER=09
  elif [ "$1" == "spring" ]; then
    SCHED_PULL_SEMESTER=01
  fi
fi
if [ -z "$SCHED_PULL_SEMESTER" -o -z "$2" ]; then
  cat pull_schedule_usage.txt
  exit -1
fi
SCHED_PULL_URL_BASE="http://sis.rpi.edu/reg/zs"
SCHED_PULL_URL_SUFF=".htm"
wget -q -O $2$1.htm $SCHED_PULL_URL_BASE$2$SCHED_PULL_SEMESTER$SCHED_PULL_URL_SUFF
SCHED_PULL_WGET_RET=$?
if [ $SCHED_PULL_WGET_RET -ne "0" ]; then
  echo -e "wget returns $SCHED_PULL_WGET_RET"
  echo -e "\e[00;31mERROR: Schedule download failed. Check that the semester and year are valid. The schedules might not be published yet. If all else fails, email hiprofessorsdd@gmail.com to report an error.\e[00m"
else
  python parse_sched.py $2$1.htm
fi
