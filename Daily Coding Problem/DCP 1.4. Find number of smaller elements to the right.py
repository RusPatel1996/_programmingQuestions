# %%
import bisect
XS = [3, 4, 9, 6, 1]


# %%
''' Brute-force solution with O(n^2) time and O(n) space '''


def bruteForce(xs):
    for i, v in enumerate(xs):
        smallerElems = 0
        for j in range(i, len(xs)):
            smallerElems += 1 if xs[j] < v else 0
        yield smallerElems


# %%
''' Faster method using sorting and insertion sort with O(n log n) time and O(n) space '''


def optimalMethod(xs):
    seen = []
    results = []

    for v in reversed(xs):
        i = bisect.bisect_left(seen, v)
        results.append(i)
        bisect.insort(seen, v)

    return reversed(list(results))


# %%
if __name__ == "__main__":
    print(list(bruteForce(XS)))
    print(list(optimalMethod(XS)))
