# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
# Make sureyou're dishing out a list by multiplying the value x by n
# For instance: # count_by(100, 5), [100, 200, 300, 400, 500])

def count_by(x, n):
    lst = []
    for y in range(1,n+1):
        lst.append(y * x)
    return lst

count_by(100, 5)
