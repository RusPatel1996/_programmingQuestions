import unittest
import random

# Decided to test my method to make sure it was functioning the same way as kadanes algorithm


class testMaxSum(unittest.TestCase):

    ''' ----------------------- '''

    def myMaxSum(self, xs):
        maxSum, runningSum = -float("inf"), 0
        for v in xs:
            if runningSum + v < 0:
                runningSum = 0
            else:
                runningSum += v
            maxSum = max(maxSum, runningSum)
        return maxSum
    ''' ----------------------- '''

    def kadanesMaxSum(self, xs):
        maxSum, runningSum = 0, 0
        for v in xs:
            runningSum = max(v, runningSum + v)
            maxSum = max(maxSum, runningSum)
        return maxSum

    def generateRandomArray(self):
        return [random.randint(0, 1000) for _ in range(100)]

    def test_isCorrect(self):
        for _ in range(10):
            randomList = self.generateRandomArray()
            kadanesSum, mySum = self.kadanesMaxSum(
                randomList), self.myMaxSum(randomList)
            self.assertEqual(mySum, kadanesSum)


unittest.main()
