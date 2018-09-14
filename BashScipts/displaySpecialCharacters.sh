#!/bin/bash
TOTARGS=$#
ARGS=$@

echo -E "Total number of arguments passed = " $TOTARGS; echo
COUNT=1
for i in $ARGS; do echo "Argument $COUNT = $i"; let COUNT+=1; done

tail -f /home/nycadm/log.file &
echo
echo -n "\$0 - The name of the Bash script = "; echo $0
echo -n "\$1 - \$9 - The first 9 arguments to the Bash script = "; echo $1
echo -n "\$# - How many arguments were passed to the Bash script = "; echo $#
echo -n "\$@ - All the arguments supplied to the Bash script = "; echo $@
echo -n "\$* - All the arguments supplied to the Bash script = "; echo $*
echo -n "\$? - The exit status of the most recently run process = "; echo $?
echo -n "\$$ - The process ID of the current script = "; echo $$
echo -n "\$! - The process ID of the most recently executed background pipeline = "; echo $!
echo -n "\$USER - The username of the user running the script = "; echo $USER
echo -n "\$HOSTNAME - The hostname of the machine the script is running on = "; echo $HOSTNAME
echo -n "\$SECONDS - The number of seconds since the script was started = "; echo $SECONDS
echo -n "\$RANDOM - Returns a different random number each time is it referred to = "; echo $RANDOM
echo -n "\$LINENO - Returns the current line number in the Bash script = "; echo $LINENO
kill -15 `echo $!`
echo $BASH_ARG0
