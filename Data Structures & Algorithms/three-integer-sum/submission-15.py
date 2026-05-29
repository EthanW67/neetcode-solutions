class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break
            left, right = i + 1, len(nums) - 1
            while left < right:
                if (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while nums[left-1] == nums[left] and left < right:
                        left += 1
                    while nums[right+1] == nums[right] and left < right:
                        right -= 1

        return result
        
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        