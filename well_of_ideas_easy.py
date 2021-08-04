# codewars challenge, check out the URL:
# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

# this solution is kind of ineffective, but one of the ways to get to the solution

def well(mylist):
    otherlist = []
    for element in mylist:
        if element == 'good':
            otherlist.append(element)
    if len(otherlist) == 0:
        return 'Fail!'
    elif len(otherlist) <= 2:
        return 'Publish!'
    elif len(otherlist) >= 2:
        return 'I smell a series!'

# I stumbled on this one later, which I like significantly more
# This count function is really cut for the purpose.

# def well(x):
#     if x.count("good") == 0:
#         return "Fail!"
#     elif x.count("good") <= 2:
#         return "Publish!"
#     else:
#         return "I smell a series!"

well(['bad', 'bad', 'bad', 'bad', 'bad'])
# For every good kata idea there seem to be quite a few bad ones!

# In this kata you need to check the provided array (x) 
# for good ideas 'good' and bad ideas 'bad'. 
# If there are one or two good ideas, return 'Publish!'
# , if there are more than 2 return 'I smell a series!'.
# If there are no good ideas, as is often the case, return 'Fail!'.


