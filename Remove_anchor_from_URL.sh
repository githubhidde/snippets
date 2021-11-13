#!/bin/bash

# codewars challenge, check out the URL:
# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/shell

# Complete the function/method so that it returns the url 
# with anything after the anchor (#) removed. 


Remove_anchor_from_URL () {
echo $1 | cut -d'#' -f1
}

Remove_anchor_from_URL $1

# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"


