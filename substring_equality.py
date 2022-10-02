import random


def substring_equality(string, a, b, l):
    """
    quickly find if a substring1 and substring2 are equal
    :param string:
    :param a: start index if substring1
    :param b: start index of substring2
    :param l: equal length of each substring
    :return: 1 -- yes, 0 -- no
    """
    m1, m2 = 10 ** 9 + 7, 10 ** 9 + 9
    x = random.randint(1, 10 ** 9)

    h1 = precompute_hashes(string, x, m1)
    h2 = precompute_hashes(string, x, m2)

    sub_1_m1 = h1[a + l] - x ** l * h1[a]
    sub_2_m1 = h1[b + l] - x ** l * h1[b]
    sub_1_m2 = h2[a + l] - x ** l * h2[a]
    sub_2_m2 = h2[b + l] - x ** l * h2[b]

    if sub_1_m1 % m1 == sub_2_m1 % m1 and sub_1_m2 % m2 == sub_2_m2 % m2:
        return 1

    return 0


def precompute_hashes(string, x, m):
    hashes = [None] * (len(string) + 1)

    # due to recursive calc of the hash; init w/ dummy to allow proper indexing
    hashes[0] = 0

    # we do 1 more because otherwise 1st char is left 0
    for i in range(1, len(string) + 1):
        hashes[i] = (x * hashes[i - 1] + ord(string[i - 1])) % m

    return hashes
