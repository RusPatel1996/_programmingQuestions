def maxSubArraySum(nums, i, maxSeen, size):
    if i == size:
        return maxSeen
    nums[i] = max(nums[i] + nums[i-1], nums[i])
    maxSeen = max(maxSeen, nums[i])
    return maxSubArraySum(nums, i+1, maxSeen, size)

def maxSubArray(nums):
    if len(nums) == 0: return None
    if len(nums) == 1: return nums[0]
    return maxSubArraySum(nums, 1, nums[0], len(nums))

if __name__ == "__main__":
    xs = [3, 2, -6, 3, 8]
    print(maxSubArray(xs))