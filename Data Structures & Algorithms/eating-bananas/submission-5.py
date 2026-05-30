class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            middle = (left + right) // 2
            hours = 0 
            for p in piles:
                hours += math.ceil(p / middle)
            if hours <= h:
                result = min(middle, result)
                right = middle - 1
            else:
                left = middle + 1
        return result