class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if nums == 0:
                currMin, currMax = 1, 1
            tempMax = currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num * tempMax, num * currMin, num)
            result = max(currMax, result)
        return result