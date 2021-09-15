# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5865918c6b569962950002a1/train/python

# This Kata is intended as a small challenge for my students

# All Star Code Challenge #18

# Create a function that accepts 2 string arguments 
# and returns an integer of the count of occurrences the 2nd argument 
# is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0

# Notes:

#     The first argument can be an empty string
#     The second string argument will always be of length 1 

def str_count(strng, letter):
    # Reading this challenge, everything is pointing to a construct
    # where you have to set a variable where you can collect
    # matches of an equation in. Like a rain barrel.
    # Let's call the variable counter.
    counter = 0
    # A for loop to actually set up the equation is common good.
    for letter_in_strng in range(len(strng)):
        # Here we compare the letters in the string with the given var
        if strng[letter_in_strng] == letter:
            # to finish of we add up the matches
            counter += 1
    # Here you have it. Just return you're collection of rain drops.
    return counter

str_count('hello', 'h')



