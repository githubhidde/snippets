# codewars challenge, check out the URL:
# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

def name_shuffler(str_):
    # Let's split the string to work from there
    str_ = str_.split()
    # print(str_)
    # I want to work with a for loop to actually swap the values
    # An empty string is handy to cath the individual values
    swapped_string = ''
    # So here we go. Let's reverse the string before looping.
    # You want to capture the last name and first name in the right order.
    for word in reversed(str_):
        # swapped_string += word + ' ' --> is the same as
        # swapped_string = swapped_string + word + ' '
        swapped_string += word + ' '
    # Major drawback of this approach is the last whitespace
    # directly after the first name. With slicing we just cut if off;)
    return swapped_string[:-1]

name_shuffler('john McClane')

# Write a function that returns a string in which 
# firstname is swapped with last name.

# name_shuffler('john McClane'); => "McClane john"
