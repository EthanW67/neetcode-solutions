class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev, curr = 0, 0
        for i in range(len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr