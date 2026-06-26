class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        result = 0
        total = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                result = i + 1
        return result