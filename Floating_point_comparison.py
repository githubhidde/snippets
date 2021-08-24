# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8/train/python

   # Task

   # You have:

   #     a float value that comes from a computation 
   #     and may have accumulated errors 
   #     p to ±0.001
   #     a reference value

   #     a function approx_equals that compare the two values taking into account 
   #     loss of precision; the function should return True if and only if 
   #     the two values are close to each other, the maximum allowed difference 
   #     is 0.001
   
def approx_equals(a, b):
   # Below you see a function that's given, 
   # but fails on executing the job decently

   # a = round(a, 3)
   # b = round(b, 3)
   # return a == b
   import math
   return math.isclose(a, b, abs_tol = 0.001)


approx_equals(123.2345, 123.234501)

# @test.describe('Fixed tests')
# def fixed_tests():
#     data = (
#         (175.9827, 82.25, False),
#         (-156.24037, -156.24038, True),
#         (123.2345, 123.234501, True),
#         (1456.3652, 1456.3641, False),
#         (-1.234, -1.233999, True),
#         (98.7655, 98.7654999, True),
#         (-7.28495, -7.28596, False))







