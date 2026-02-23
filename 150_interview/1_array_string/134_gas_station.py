# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost,
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.

from typing import List


class Solution:
    def canCompleteCircuit_bad(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff_table = []
        for i in range(len(gas)):
            diff_table.append(sum([gas[j] - cost[j] for j in range(0, i + 1)]))
        min_index = 0
        min_val = float("inf")

        for i in range(len(diff_table)):
            if diff_table[i] < min_val:
                min_index = i
                min_val = diff_table[i]
        return min_index + 1 if min_index != len(diff_table) - 1 else 0

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        current = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            current += diff

            if current < 0:
                current = 0
                start = i + 1
        return start if total >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
assert Solution().canCompleteCircuit(gas, cost) == 3


gas = [2, 3, 4]
cost = [3, 4, 3]
print(Solution().canCompleteCircuit(gas, cost))
assert Solution().canCompleteCircuit(gas, cost) == -1
