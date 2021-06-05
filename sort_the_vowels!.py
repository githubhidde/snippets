def sort_vowels(s):
    # First we have to define vowels
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    # A list to collect the manipulated strings
    collector = []
    # Looping through the string is sufficient.
    # First we have to exclude non string input
    if type(s) != str:
        return ''
    # Ok done, we'll loop through string input now.
    if type(s) == str:
        # Test the letters in the string against the vowels in the list
        for letter in s:
            if letter in vowels and s:
                # Manipulate the strings as asked
                letter = '|' + letter
                # Append them to the collector list
                collector.append(letter)
            # Letters which are not vowel flow automatically through
            elif letter not in vowels and s:
                # Manipulate the strings as asked
                letter = letter + '|'
                # Append them to the collector list
                collector.append(letter)
        # Simply use the join function to string the letters
        # from the list together with the '\n' as a binder.
        vowels_sorted = '\n'.join(collector)
        # There you have it.
        return vowels_sorted

sort_vowels(None)

