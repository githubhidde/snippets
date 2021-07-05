def count_by(x, n):
    lst = []
    for y in range(1,n+1):
        lst.append(y * x)
    return lst




count_by(100, 5)

# @test.describe('next_item')
# def test_next_item():
#     @test.it('should pass some tests')
#     def tests():
#         test.assert_equals(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
#         test.assert_equals(next_item(['a', 'b', 'c'], 'd'), None)
#         test.assert_equals(next_item(['a', 'b', 'c'], 'c'), None)
#         test.assert_equals(next_item('testing', 't'), 'e')
#         test.assert_equals(next_item(iter(range(1, 30000)), 12), 13)
