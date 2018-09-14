#!/bin/bash
# Name: reset_passwd.sh
user=$1
if [ $# -ne 1 ]; then
     echo "Usage: ./reset_passwd.sh  username"
     exit 1
fi
if [ `grep $user /etc/shadow | cut -d: -f2 | sed 's/.*\(LK\).*/\1/'` = "LK" ]; then
     echo "This user account is locked."
     echo -n "Should I unlock it? Y or N "
     read locked
     if [ -n $locked ] && [ $locked = "Y" -o $locked "y" ]; then
          passwd - u $user
          echo "$user has been unlocked."
     else
          exit
     fi
else
     exit
fi