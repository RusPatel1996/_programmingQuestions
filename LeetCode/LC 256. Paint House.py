from heapq import nsmallest


class Solution:
    # Get two lowest values of the three colors in a row with their respective position
    def getMinimums(self, row):
        return nsmallest(2, enumerate(row), key=lambda a: a[1])

    def helper(self, costs, row, smallest, second_smallest):
        if row < 0:
            # First row should have all the optimal values so just return the smallest
            return smallest[1]

        for i, v in enumerate(costs[row]):
            # Remember this will always update two values since it is the minimum
            if i != smallest[0]:
                costs[row][i] = v + smallest[1]

            # Updates where the indexes are the same for the minimum with the second smallest
            else:
                costs[row][i] = v + second_smallest[1]

        smallest, second_smallest = self.getMinimums(
            costs[row])  # in the form of (index, value)
        return self.helper(costs, row-1, smallest, second_smallest)

    def minCost(self, costs: list) -> int:
        if costs == []:
            return 0
        row = len(costs) - 1
        smallest, second_smallest = self.getMinimums(
            costs[row])  # in the form of (index, value)
        return self.helper(costs, row-1, smallest, second_smallest)


if __name__ == "__main__":
    solution = Solution()
    xs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(solution.minCost(xs))
    