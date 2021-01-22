def maxSubarraySum(xs):
    maxSum, runningMax = -float("inf"), 0
    for v in xs:
        runningMax = max(v, runningMax + v)
        maxSum = max(maxSum, runningMax)
    return maxSum


def minSubarraySum(xs):
    minSum, runningMin = float("inf"), 0
    for v in xs:
        runningMin = min(v, runningMin + v)
        minSum = min(minSum, runningMin)
    return minSum


if __name__ == "__main__":
    xs = [-3, -2, -1]

    if all(x < 0 for x in xs):
        print(max(xs))
    else:
        maxWrapedSubarraySum = sum(xs) - minSubarraySum(xs)
        print(max(maxWrapedSubarraySum, maxSubarraySum(xs)))
