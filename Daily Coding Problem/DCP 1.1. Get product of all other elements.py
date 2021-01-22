''' First Approach '''

from itertools import accumulate
from functools import reduce
from operator import mul

xs = [1, 2, 3, 4, 5]

totalProduct = reduce(mul, xs)

for i, v in enumerate(xs):
    xs[i] = totalProduct / v

print(xs)


''' Second Approach '''


xs = [1, 2, 3, 4, 5]

prefixProd = list(accumulate(xs, mul))
suffixProd = list(accumulate(reversed(xs), mul))

ys = []

for i, v in enumerate(xs):
    if i == 0:
        ys.append(suffixProd[-2])
    if i == len(xs) - 1:
        ys.append(prefixProd[-2])
    if i > 0 and i < len(xs)-1:
        ys.append(prefixProd[i-1] * suffixProd[len(xs)-1-i-1])

print(ys)
