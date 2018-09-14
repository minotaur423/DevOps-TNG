#!/bin/bash
user=$1
if [ $# -ne 1 ]; then
      echo "Usage: ./reset_passwd.sh  username"
      exit 1
fi
if [ `grep $user /etc/shadow | cut -d: -f2 | sed 's/.*\(LK\).*/\1/'` = "LK" ]; then
      echo "This user account is locked."
      echo -n "Should I unlock it? Y or N "
      read locked
      if [ -z $locked ]; then
         echo "You must enter Y or N:

      passw -u $user
      echo "Now it is unlocked."
fi
