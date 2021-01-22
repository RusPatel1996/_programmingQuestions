class Solution1:
    def minCostClimbingStairs(self, cost) -> int:
        cost.append(0)
        return self.helper(cost, {}, len(cost)-1)

    def helper(self, cost: list, cache: dict, n: int) -> int:
        if n == 0 or n == 1:
            return cost[n]

        if n not in cache:
            cache = {
                n: cost[n] + min(self.helper(cost, cache, n-1), self.helper(cost, cache, n-2))}

        return cache[n]


#----------------------------------------------------------------#
# TLE so let's optimize using variables to store previous two values
class Solution2:
    def minCostClimbingStairs(self, cost) -> int:
        cost.append(0)
        return self.helper(cost, 0, 0, len(cost)-1)

    def helper(self, cost, prev_1, prev_2, n) -> int:
        if n == 0 or n == 1:
            return cost[n]

        prev_1 = self.helper(cost, prev_1, prev_2, n-1)
        prev_2 = self.helper(cost, prev_1, prev_2, n-2)

        return cost[n] + min(prev_1, prev_2)


#----------------------------------------------------------------#
# TLE by Max Recursion exceeded so let's Optimize by using a For loop
# and variables to store previous two values
class Solution3:
    def minCostClimbingStairs(self, cost) -> int:
        prev_1, prev_2 = cost[0], 0
        curr = 0

        for i in range(1, len(cost)):
            curr = cost[i] + min(prev_1, prev_2)
            prev_2 = prev_1
            prev_1 = curr
        
        return min(prev_1, prev_2)


if __name__ == "__main__":
    solution = Solution1()
    xs = [2,3,8]

    print(solution.minCostClimbingStairs(xs))
