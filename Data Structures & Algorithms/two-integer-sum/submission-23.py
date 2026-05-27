class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for num in range(len(nums)):
            dict1[nums[num]] = num

        for i in range(len(nums)):
            value = target - nums[i]
            if value in dict1 and dict1[value] != i:
                return [i, dict1[value]]
        