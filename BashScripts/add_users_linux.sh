#!/bin/bash
# Script Name: add_users_linux.sh
# Script Purpose: Add users to Linux server.

users=$*
if [ $# -lt 1 ]; then
        echo "Usage: ./add_users username1 username2 usernameN"
        exit 1
fi
read -p "Enter group for users: " group
if [ "`cat /etc/group | grep $group | awk -F: '{print $1}';`" != "$group" ]; then
        groupadd $group
        printf "Group $group did not exist but was created successfully.\n"
fi
read -s -p "Enter temporary password for users: " pass; echo -e "\n"
enc_passwd=$(perl -e 'print crypt($ARGV[0], "password")' $pass)
for user in $users; do
        useradd -m -d /export/local/$user -g $group -s /bin/bash -p $enc_passwd $user
        echo -e "User account $user created and added to group $group."
done