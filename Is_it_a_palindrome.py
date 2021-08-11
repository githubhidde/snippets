# codewars challenge, check out the URL:
# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

# A palindrome is a word, number, phrase, or other sequence of 
# characters which reads the same backward as forward, 
# such as madam or racecar. 

def is_palindrome(s):
# With slicing you'll might immediately reverse a string
# compare it with the original input and you're set.
# But be watchfull about converting the string to normal letters only
# straight away

# This is what's going on behind the scenes
    s = s.lower()
    if s[::-1] == s:
        return True
    else:
        return False
# More efficient is to jot it down like this
    return s == s[::-1]

is_palindrome('mealam')

# @test.describe('sample tests')
# def sample_tests():
#     test.assert_equals(is_palindrome('a'), True)
#     test.assert_equals(is_palindrome('aba'), True)
#     test.assert_equals(is_palindrome('Abba'), True)
#     test.assert_equals(is_palindrome('malam'), True)
#     test.assert_equals(is_palindrome('walter'), False)
#     test.assert_equals(is_palindrome('kodok'), True)
#     test.assert_equals(is_palindrome('Kasue'), False)