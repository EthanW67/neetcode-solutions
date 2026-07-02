class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0] * (n + 2)
        result[n] = 1
        result[n+1] = 0
        for i in range(n-1, -1, -1):
            result[i] = result[i+1] + result[i+2]
            
        return result[0]
