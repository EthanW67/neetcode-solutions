class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, temps = stack.pop()
                result[index] = idx - index
            stack.append((idx, temp))
        return result