# codewars challenge, check out the URL:
# https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python

# Very simple, given a number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    
    number = str(number)
    if number[0] == '-':
        return float(number[1:])
    if number[0] != '-':
        return float('-' + number)

opposite(3.1458)

# import codewars_test as test
# from solution import opposite

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(opposite(1),-1)
#         test.assert_equals(opposite(25.6), -25.6)
#         test.assert_equals(opposite(0), 0)
#         test.assert_equals(opposite(1425.2222), -1425.2222)
#         test.assert_equals(opposite(-3.1458), 3.1458)
#         test.assert_equals(opposite(-95858588225),95858588225)
