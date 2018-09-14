#!/bin/bash
# Name: add_accounts.sh
echo -n "Enter the number of users to add: "
read amt
count=1
while [ $count -le $amt ]; do
        useradd -m -d /export/home/user$count -s /bin/bash -c "User$count Login" -g usergrp user$count
        echo "User$count Created."
        let count+=1
done