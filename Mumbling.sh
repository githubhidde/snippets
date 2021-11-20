#!/bin/bash

# Check the url: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/shell

accum () {
answer=""
for (( i=0; i<${#1}; i++ ))
do
cardboard_box=${1:${i}:1}
letterSpaced=$(printf "%$((i+1))s" "$cardboard_box")
letterStringed=${letterSpaced// /$cardboard_box}
letterStringed=${letterStringed,,}-
letterStringed=${letterStringed^}
answer+=$letterStringed
done
echo ${answer::-1}
}
accum "abc"