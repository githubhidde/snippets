# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

# Although it could be tempting to try to figure out a for loop,
# it pays off to be a little creative;)

def century(year):
    return (year + 99) // 100

century(1601)

# Introduction

# The first century spans from the year 1 up to and including the year 100, 
# The second - from the year 101 up to and including the year 200, etc.
# Task :

# Given a year, return the century it is in.

# Examples:
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 356  --> 4