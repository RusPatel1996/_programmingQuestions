def climbStairs(n, cache):
    if n <= 2: return n
    if n not in cache:
        cache[n] = climbStairs(n-1, cache) + climbStairs(n-2, cache)
    return cache[n]

if __name__ == "__main__":
    n = 5
    cache = {}
    print(climbStairs(n, cache)) # --> 8
    print(cache) # --> {3:3, 4:5, 5:8}