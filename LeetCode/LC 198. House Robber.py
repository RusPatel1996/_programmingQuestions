def helperfunc(nums, i, n, maxSeen):
    if i == -1:            
        return max(nums[0], nums[1])
    
    if i != n-1 and i != n-2:
        nums[i] = nums[i] + maxSeen
        maxSeen = max(maxSeen, nums[i+1])
        
    return helperfunc(nums, i-1, n, maxSeen)
    

def rob(nums):
    n = len(nums)
    
    if n == 0: return 0
    if n == 1: return nums[0]
    
    return helperfunc(nums, n-1, n, nums[n-1])

if __name__ == "__main__":
    xs = [2,7,9,3,1]

    print(rob(xs)) # --> 12