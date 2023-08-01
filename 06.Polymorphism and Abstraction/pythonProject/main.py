from itertools import permutations


def possible_permutations(in_list):
    for i in permutations(in_list):
        yield list(i)
