# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python

# In Python you don't habe a build in switch statement and you might
# figure that series of if-else-if blocks will do it for you.

# It's recommendable though to use to powerful dictionary mappings
# While each condition has to be looked up sequentially in contrary
# to a dictionary where the expression has to be evaluated once
# to jump to the appropriate branch of code that has to be executed. 
def switch_it_up(number):
    switcher = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    for key, value in switcher.items():
        return switcher[number]

switch_it_up(0)

# When provided with a number between 0-9, return it in words.

# Input :: 1

# Output :: "One".

# If your language supports it, try using a switch statement.



