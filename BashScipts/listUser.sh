#!/bin/bash
if [ $# -ne 1 ]; then
        echo "Usage: listUser.sh username"
        exit 1
fi

for i in `cat /etc/passwd | awk -F: '{print $1}'`
	do 
		if [ "$i" == "$1" ]; then
			echo "Username $1 exists."
		else
			echo "Username $1 does not exist."
		fi
	done

echo "This is the first parameter: $1"
echo "The number of arguments is: $#"
