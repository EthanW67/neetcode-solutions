class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        amount = 0
        for i in range(len(nums)):
            amount += nums[i]
            maxSub = max(amount, maxSub)
            if amount < 0:
                amount = 0
                        
        return maxSub