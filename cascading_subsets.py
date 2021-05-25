# Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

# each_cons([1,2,3,4], 2)
#   #=> [[1,2], [2,3], [3,4]]

# each_cons([1,2,3,4], 3)
#   #=> [[1,2,3],[2,3,4]]
  
def each_cons(lst, n):
    i = 0
    result = []
    while i < len(lst) - n + 1:
        result.append(lst[i:i + n])
        i += 1
    return result

each_cons([3, 5, 8, 13], 2)
