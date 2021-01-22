''' First Approach '''

xs = [3, 7, 5, 6, 9]

ys = sorted(xs)

left, right = None, None

for i, v in enumerate(xs):
    if v != ys[i] and left is None:
        left = i
    elif v != ys[i]:
        right = i

print((left, right))


''' Second Approach '''

xs = [3, 7, 5, 6, 9]

left, right = None, None
minSeen, maxSeen = float("inf"), -float("inf")

for i, v in enumerate(xs):
    maxSeen = max(maxSeen, v)
    if v < maxSeen:
        right = i

for i, v in reversed(list(enumerate(xs))):
    minSeen = min(minSeen, v)
    if v > minSeen:
        left = i

print((left, right))
