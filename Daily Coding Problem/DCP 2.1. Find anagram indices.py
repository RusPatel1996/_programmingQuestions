''' Naive Solution with time of O(nk) and space of O(k) '''

from collections import Counter


def anagram_indices(w, s):
    window_size = len(w)
    w_dict = Counter(w)

    for i in range(len(s) - (window_size-1)):
        window = s[i: i + window_size]
        window_dict = Counter(window)
        if w_dict == window_dict:
            yield i


print(list(anagram_indices("", "abxaba")))


''' More optimal solution '''
