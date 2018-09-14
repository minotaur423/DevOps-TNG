#!/bin/bash
TOTARGS=$#
ARGS=$@

echo "Total arguments passed = $TOTARGS"; echo
COUNT=1
for i in $ARGS; do echo "Argument $COUNT = $i"; let COUNT+=1; done
