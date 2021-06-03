def logical_calc(array, op):
    res = array[0]
    for x in array[1:]:
        if op == "AND":
            res &= x
        if op == "OR":
            res |= x
        if op == "XOR":
            res ^= x
        
    return res

logical_calc([True, False], "XOR")
# test.describe('Basic tests')
# test.assert_equals(logical_calc([True, False], "AND"), False)
# test.assert_equals(logical_calc([True, False], "OR"), True)
# test.assert_equals(logical_calc([True, False], "XOR"), True)

# test.assert_equals(logical_calc([True, True, False], "AND"), False)
# test.assert_equals(logical_calc([True, True, False], "OR"), True)
# test.assert_equals(logical_calc([True, True, False], "XOR"), False)

