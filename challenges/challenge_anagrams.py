def sorting_strings(string):
    letters = string.lower()
    counter = 0
    modify = True

    while modify:
        modify = False
        for index in range(len(letters) - counter - 1):
            if letters[index] > letters[index + 1]:
                letters[index], letters[index + 1] = \
                    letters[index + 1], letters[index]
                modify = True
        counter += 1
    return letters


def is_anagram(first_string, second_string):

    if first_string == '' or second_string == '':
        return (first_string, second_string, False)

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    string1 = sorting_strings(first_string)
    string2 = sorting_strings(second_string)

    if string1 == string2:
        return (string1, string2, True)
    else:
        return (string1, string2, False)
