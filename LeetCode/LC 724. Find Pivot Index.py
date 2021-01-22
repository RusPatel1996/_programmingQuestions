from itertools import accumulate

class Solution:
    def pivotIndex(self, nums):
        ltorSum = list(accumulate(nums))
        nums.reverse()
        rtolSum = list(accumulate(nums))
        rtolSum.reverse()
        for i in range(0, len(ltorSum)):
            if ltorSum[i] == rtolSum[i]:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([1, 7, 3, 6, 5, 6])) # --> 3