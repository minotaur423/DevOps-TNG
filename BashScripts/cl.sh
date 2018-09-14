#!/bin/bash
if [ $# -ne 2 ]; then
        echo "Usage: cl.sh first_name user_name"
        exit 1
fi
echo "This is the first parameter: $1"
echo "This is the second parameter: $2"
echo "The number of arguments is: $#"