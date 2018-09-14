#!/bin/bash
#
#  This script must show the date and time, list all logged-in users,
#+ and give the system uptime.  Finally, it must save all this
#+ information to a logfile

LOG_DIR=/var/log
CURDATE=`date`
LIUSERS=`who`
SYSUPTIME=`uptime`
LOG_FILE=MyScript.log
#  Get date and time.
echo -e "$CURDATE\n\n$LIUSERS\n\n$SYSUPTIME\n" | tee -a $LOG_DIR/$LOG_FILE
exit 0