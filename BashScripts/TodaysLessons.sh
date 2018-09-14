printf "%-14.14s%-16.16s%-20.20s%-15.15s%-6.6s%-5.5s\n" "First Name" "Surname" "Address" "City" "ST" "Zip"
echo ============================================================================
sort -t : -k2 $fname | awk -F: '{printf("%-14.14s%-16.16s%-20.20s%-15.15s%-6.6s%-5.5s\n", $1, $2, $3, $4, $5, $6)}'


[nycadm@sym1 bin]$ cat grepscript
#!/bin/bash
file=greptest
echo "Lines that start with a T:"
grep "^T" $file
echo =============================================================================
echo -n "Blank lines: "; grep -c "^$" $file
grep "^$" $file
echo =============================================================================
echo "Lines that have two or more a's anywhere in them:"
grep -E "aa" $file
echo =============================================================================
echo "Lines that have a two-or-more-digit number in them:"
grep '[0-9][0-9]' $file
echo =============================================================================
echo "Lines that have the pattern [x,y] in them, where x and y are any numbers:"
grep -E '\[[0-9]+,[0-9]+\]' $file
echo =============================================================================

[nycadm@sym1 bin]$ cat formatwhoscript
#!/bin/bash
who | awk '{printf("%-15s%s %2s %s\n", $1, $3, $4, $5)}'

[nycadm@sym1 bin]$ cat greptest
This is the first line in the file

and this is the second

This line has a sequence of a's in it: aaaaa

vector [1,4]


This is line 10
This is line 11

vector2 [x,y]
vector3 [,345]  this line should not be seen in the last solution
vector4 [14,55]
[nycadm@sym1 bin]$
