# codewars challenge, check out the URL:
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    # I googled around how I could easily count given values,
    # but couldn't figure out how to use an advanced technique like
    # a function or list comprehension.
    # That's why I used the generic approach below.
    # Easy to understand for fellow beginners.
    ja = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm']
    nee = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x',
    'y', 'z']
    approved = []
    disapproved = []
    for letter in s:
        if letter in ja:
            approved.append(letter)
        if letter in nee:
            disapproved.append(letter)
    return str(len(disapproved)) + '/' + str(len(disapproved) + len(approved))

printer_error('abcxyz')

# In a factory a printer prints labels for boxes. 
# For one kind of boxes the printer has to use colors which, 
# for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. 
# For example a "good" control string would be aaabbbbhaijjjm 
# meaning that the printer used three times color a, 
# four times color b,  one time color h then one time color a...

# Sometimes there are problems: 
# lack of colors, technical malfunction and a "bad" control string is 
# produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which
 # given a string will
# return the error rate of the printer as a 
# string representing a rational whose numerator is the 
# number of errors and the denominator the length of the control
 # string. 
# Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and 
# contains only letters from a to z.
# Examples:

# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"


