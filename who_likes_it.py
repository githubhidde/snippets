# codewars challenge, check out the URL:
# https://www.codewars.com/kata/5865918c6b569962950002a1/train/python

def likes(names):
    # If there are no values in the argument, it's given what you should return
    if not names:
        return 'no one likes this'
    # If there are values available, we have to evaluate the number of them
    # When there is only name it's foreseeable what you have to do.
    if names:
        if len(names) == 1:
            for name in names:
                return f"{name} likes this"
        multiple_names = []
    # It's getting heavier, when you have to format 2 likes.
        if len(names) <= 2:
    # I choose to loop through the names, add them to an empty list
    # and then join them together, before returning the string.
            for name in names:
                multiple_names.append(name)
            returner = ' and '.join(multiple_names)
            return f"{returner} like this"
    # When it's about 3 names, it's again another ball game.
    # Again we loop through the names, append them to the empty list,
    # but we actually use slicing in order to prepare the formatting
    # before putting it out
        if len(names) <= 3:
            for name in names[0:1]:
                multiple_names.append(name)
                returner = ' and '.join(multiple_names)
            for name in names[1:2]:
                multiple_names.append(name)
                returner_with_a_comma = ', '.join(multiple_names)
            for name in names[2:3]:
                multiple_names.append(name[2:3])
                name = ' and ' + name
                returner = ' and '.join(name)
                return f"{returner_with_a_comma}{name} like this"
    # When it's about 4 names, I just choose to follow the assignemnt literally
    # That is filtering the first 2 names out.
    # Putting them together with a seperated comma
        if len(names) >= 4:
            for name in names[0:1]:
                multiple_names.append(name)
                returner = ' and '.join(multiple_names)
    # the 'others' can be defined by subtracting the first two names from
    # the total of likes.
    # Then you're ready to return the result
    # I enumerate therefore the list, with that you have integers assigned
    # resembling the total number of total included in the array.
            for number, name in enumerate(names[1:2]):
                multiple_names.append(name)
                returner_with_a_comma = ', '.join(multiple_names)
                number = len(names) - 2
                return f"{returner_with_a_comma} and {number} others like this"

likes([])