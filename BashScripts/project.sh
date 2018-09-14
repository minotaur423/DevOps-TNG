#!/bin/bash
############################################################################
# This program will create an application for tracking people's contact    #
# details, such as name and address. This will be a menu-based program,    #
# with a main screen offering the user the options to create, view, search #
# for, and delete contact details. All details will be stored in a text    #
# file.                                                                    #
#   * The program will prompt the user for six items of data:              #
#     * First name, Surname, Address, City, State, Zip                     #
#   * The program will append the date to the end of a text file, all on   #
#     one line, separated by the ":" character.                            #
#   * There will be a variable called fname that will store the name of    #
#     the file into which all this information will be written.            #
#   * The value of this variable can be something like personnel.dat.      #
#   * Before the program exits, it will display the contents of the file,  #
#     as well as a count of the number of records in the file.             #
#   * The project will be fully commented.                                 #
############################################################################
#
# Define the name of the file.
fname=personnel.dat

# If the file does not exist, create it.
[ ! -f $fname ] && > $fname

# Display the menu.
clear
echo -e "\n\tShell Programming Database\n"
echo -e "\t\tMain Menu"
echo -e "\t1. Create a record"
echo -e "\t2. View records"
echo -e "\t3. Search for records"
echo -e "\t4. Delete records that match a pattern\n"
echo -n -e "\tYour selection: "; read selection
clear
case $selection in
        1)
                echo -e "You selected to create a new record.\n"
                # Request contact details: First name, Surname, Address, City, State, Zip
                while [ -z "$name" ]
                do
                        echo -n "Please enter your first name: "; read name
                done
                while [ -z "$last_name" ]
                do
                        echo -n "Please enter your last name: "; read last_name
                done
                while [ -z "$address" ]
                do
                        echo -n "Please enter your address: "; read address
                done
                while [ -z "$city" ]
                do
                        echo -n "Please enter your city: "; read city
                done
                while [ -z "$state" ]
                do
                        echo -n "Please enter your state: "; read state
                done
                while [ -z "$zip" ]
                do
                        echo -n "Please enter your zip code: "; read zip
                done
                person="$name:$last_name:$address:$city:$state:$zip"
                echo $person >> $fname
                echo "Record created successfully."
                ;;
        2)
                echo -e "You selected to view records.\n"
                if [ -e "$fname" ]; then
                        echo "Here are the contacts in the database:"
                        echo
                        cat $fname | more
                        echo -e "\nThere are `cat $fname | wc -l` contacts in the database."
                else
                        echo "No records have been entered yet."
                fi
                ;;
        3)
                echo -e "You selected to search for records.\n"
                ;;
        4)
                echo -e "You selected to delete records that match a pattern.\n"
                echo -n "Enter first and last name of user you want to delete: "; read name last_name
                while [ -z "$name" ] || [ -z "$last_name" ]
                do
                        echo -n "Invalid name. Enter first name and last name: "; read name last_name
                done
                grep "$name:$last_name" $fname > /dev/null
                if [ "$?" -eq 0 ]; then
                        sed -i "/$name:$last_name/d" $fname
                        echo "The user $name $last_name has been deleted."
                else
                echo "User does not exist!"
                fi
                ;;
        *)
                echo "Invalid selection. Try again."
                exit
                ;;
esac