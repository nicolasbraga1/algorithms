def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array.pop(0)
        bigger = []
        smaller = []
        for word in array:
            smaller.append(word) if word <= pivo else bigger.append(word)
        return quicksort(smaller) + [pivo] + quicksort(bigger)


def is_anagram(first_string, second_string):
    sort_first = ''.join(quicksort(list(first_string.lower())))
    sort_second = ''.join(quicksort(list(second_string.lower())))
    if not sort_first or not sort_second:
        return sort_first, sort_second, False
    else:
        return sort_first, sort_second, sort_first == sort_second
