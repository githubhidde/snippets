# codewars challenge, check out the URL:
# https://www.codewars.com/kata/56efc695740d30f963000557/train/python
def to_alternating_case(string):
    # First things first. Integers should be unaffected by the function.
    # In the testcases it's pretty clear that integers are just converted to string.
    # So I went ahead and converted them right away.
    # They are unaffected by checking on lowercase or uppercase characteristics.
    string = str(string)
    # when it's about alternating it's easy to use a empty string to collect
    # the converted letters 
    to_alternating_case = ''
    # A for loop trough the range of the string is a handy tool to convert
    # the letters right away by their counterparts.
    # Great advantage is the fact it just passes whitespaces, numbers etc.
    for letter in range(len(string)):
         if string[letter] == string[letter].upper():
            to_alternating_case = to_alternating_case + string[letter].lower()
         else:
            to_alternating_case = to_alternating_case + string[letter].upper()
    # There you have it. You converted string.
    return to_alternating_case

to_alternating_case(12345)
# Define String.prototype.toAlternatingCase 
# (or a similar function/method such as to_alternating_case/
#     toAlternatingCase/ToAlternatingCase in your selected language; 
#     see the initial solution for details) 
# such that each lowercase letter becomes uppercase and 
# each uppercase letter becomes lowercase. For example:

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() 
# === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"




