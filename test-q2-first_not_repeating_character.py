def first_not_repeating_character(s):
    dictionary = {}

    # Stuff the entire thing in the dictionary
    for char in s:
        if char in dictionary: 
            dictionary[char] += 1
        else: 
            dictionary[char] = 1

    for char in s:
        if dictionary[char] == 1:
            return char
    
    return '_'

s = "abacabad"
print(first_not_repeating_character(s))


