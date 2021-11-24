def str_count(strng, letter):
    counter = 0
    for character in strng:
        if character == letter:
            counter = counter + 1
    return counter


print(str_count('helllllllo', 'l'))