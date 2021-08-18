# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python

# All of the animals are having a feast! Each animal is bringing one dish. 
# There is just one rule: the dish must start and end with the same letters 
# as the animal's name. For example, the great blue heron is bringing garlic 
# naan and the chickadee is bringing chocolate cake.

# Write a function feast that takes the animal's name and dish as arguments 
# and returns true or false to indicate whether the beast is allowed to bring 
# the dish to the feast.

# Assume that beast and dish are always lowercase strings, 
# and that each has at least two letters. beast and dish may contain hyphens 
# and spaces, but these will not appear at the beginning or end of the string. 
# They will not contain numerals.

def feast(beast, dish):
    # important to know is that slicing is an easy way to get the first- 
    # and last character of a string.

    # print(beast[:1])
    # print(beast[-1:])

    # Then you can just compare the condition of the string with each other
    # Return always returns a boolean value, so you're there already.
    return beast[:1] == dish[:1] and beast[-1:] == dish[-1:]

feast("great blue heron", "garlic naan")


