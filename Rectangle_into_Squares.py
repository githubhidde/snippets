# codewars challenge, check out the URL:
# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def sqInRect(length, width):
    squares = []
    area = length * width
    if length != width:
        while area > 0:
            if length < width:
                squares.append(length)
                width = width - length
                area -= length * length
            else:
                squares.append(width)
                length = length - width
                area -= width * width
        return squares

print(sqInRect(20, 14))

sqInRect(37, 14)
# test.assert_equals(sqInRect(5, 5), None)
# test.assert_equals(sqInRect(5, 3), [3, 2, 1, 1])
# test.assert_equals(sqInRect(20, 14), [14, 6, 6, 2, 2, 2])
# test.assert_equals(sqInRect(37, 14), [14, 14, 9, 5, 4, 1, 1, 1, 1])
