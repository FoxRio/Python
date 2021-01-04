def permutations(string):
    import itertools
    x = set(itertools.permutations(string, len(string)))
    lst = []

    for i in x:
        lst.append(''.join(i))
    return lst
print(permutations("abba"))