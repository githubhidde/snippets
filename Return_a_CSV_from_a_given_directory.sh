#!/bin/bash

# See the URL: https://www.codewars.com/kata/584d9264bd1606771b0000af/train/shell

Return_a_CSV () {

# Lets roll with parameter expension wohoo
# First things first, chop the shortest match of from the end
# The actual file has to be separated from the file path. The file path remains untouched;)
FILEPATH=${1%/*}
# The file path and file are seperated now, but there is a distinction between the file
# and extensions necessary as well. I'll go ahead and rip the file and file distinction apart
# using awk. The output of the commands are getting stored in the file and extensions variable
# respectively.
FILE=$(echo ${1##*/} | awk -F'.' '{print$1}')
EXTENSION=$(echo ${1##*/} | awk -F'.' '{print$2}')

# Time to harvest!
echo $FILEPATH, $FILE, $EXTENSION
}

Return_a_CSV $1