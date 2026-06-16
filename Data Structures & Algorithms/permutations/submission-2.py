class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(subset):
            
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            for choice in nums:
                if choice not in subset:
                    subset.append(choice)
                    backtrack(subset)
                    subset.pop()


        backtrack([])
        return result