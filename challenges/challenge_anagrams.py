def merge_sort(strings, start=0, end=None):
    if end is None:
        end = len(strings)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(strings, start, mid)
        merge_sort(strings, mid, end)
        merge(strings, start, mid, end)


def merge(strings, start, mid, end):
    left = strings[start:mid]
    right = strings[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            strings[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            strings[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            strings[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            strings[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_string = [*first_string.lower()]
    second_string = [*second_string.lower()]

    merge_sort(first_string)
    merge_sort(second_string)

    string1 = "".join(first_string)
    string2 = "".join(second_string)

    if len(string1) != len(string2):
        return (string1, string2, False)

    if string1 == '' or string2 == '':
        return (string1, string2, False)

    if string1 == string2:
        return (string1, string2, True)

    else:
        return (string1, string2, False)
