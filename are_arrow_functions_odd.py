# codewars challenge, check out the URL:
# https://www.codewars.com/kata/559f80b87fa8512e3e0000f5/train/python/610a905deae55d0028e2ef8a

# Just a classic. The module operator is key here. When you'll divide a number
# by 2, you'll always have a remainer of 1 when a odd nummber is given.

# P.S. Furthermore you'll can derive from the test cases, how you should name
# the function, namely 'odds'.

def odds(numbers):
    odds = []
    for x in numbers:
        if x % 2 == 1:
            odds.append(x)
    return odds
      
find_odds([2,4,5,6,7])


