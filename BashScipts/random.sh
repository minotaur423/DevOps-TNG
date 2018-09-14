#!/bin/bash
rand_num=0
rand_num1=0
let "rand_num = $RANDOM % 6 + 1"
let "rand_num1 = $RANDOM % 6 + 1"
let "total = $rand_num + rand_num1"
echo "You rolled $rand_num $rand_num1 for a total of $total"