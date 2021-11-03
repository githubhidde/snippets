# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5894017082b9fb62c50000df/train/python

# Task

# Call two arms equally strong 
# if the heaviest weights they each are able to lift are equal.

# Call two people equally strong 
# if their strongest arms are equally strong 
# (the strongest arm can be both the right and the left)
# , and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities 
# find out if you two are equally strong.

def are_equally_strong(your_left, your_right, friends_left, friends_right):
    you = [your_left, your_right]
    friend = [friends_left, friends_right]

    if min(you) != min(friend):
        return False
    if max(you) != max(friend):
        return False
    else:
        return True

are_equally_strong(15,10,15,9)

# test.it("Basic Tests")
# test.assert_equals(are_equally_strong(10,15,15,10),True)
# test.assert_equals(are_equally_strong(15,10,15,10),True)
# test.assert_equals(are_equally_strong(10,10,10,10),True)
# test.assert_equals(are_equally_strong(15,10,15,9),False)
# test.assert_equals(are_equally_strong(10,5,5,10),True)
# test.assert_equals(are_equally_strong(1,10,10,0),False)
# test.assert_equals(are_equally_strong(10, 5, 11, 4),False)
