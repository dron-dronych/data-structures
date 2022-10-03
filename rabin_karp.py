import random


def rabin_karp_search(pat, text):
    p = 1_000_000_007
    x = random.randint(1, p - 1)

    positions = []

    phash = poly_hash(pat, p, x)

    h = precompute_hashes(text, len(pat), p, x)

    for i in range(len(text) - len(pat) + 1):
        if phash != h[i]:
            continue

        if text[i: i + len(pat)] == pat:
            positions.append(i)

    return positions


def precompute_hashes(text, pat_len, p, x):
    h = [None] * (len(text) - pat_len + 1)
    sub_string = text[len(text) - pat_len: len(text)]

    h[len(text) - pat_len] = poly_hash(sub_string, p, x)

    y = 1
    for i in range(pat_len):
        y = (y * x) % p

    for i in range(len(text) - pat_len - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + pat_len])) % p

    return h


def poly_hash(string, p, x):
    hash_ = 0

    for i in range(len(string) - 1, -1, -1):
        hash_ = (hash_ * x + ord(string[i])) % p

    return hash_
