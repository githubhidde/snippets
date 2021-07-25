# codewars challenge, check out the URL:
# https://www.codewars.com/kata/571d42206414b103dc0006a1/train/python
def arr(n=0): 
    # You'll basically have to convert an integer from a minimum valuu
    # of 0 to a max of n-1 ---> [ the numbers 0 to N-1 ]
    # a plain for loop is extremely suitable
    # P.S. The test case is checking for function calls without argument
    # that's why I assign an argument '0' in the function call.
    lijst = []
    for i in range(0,n):
        lijst.append(i)
    return lijst

arr()