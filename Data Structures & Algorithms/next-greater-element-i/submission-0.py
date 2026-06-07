class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        stack = []
        freq = {}
        for i in range(len(nums2)):
            
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()
                freq[num] = nums2[i]
            stack.append(nums2[i])

        for val in range(len(nums1)):
            if nums1[val] in freq:
                result.append(freq[nums1[val]])
            else:
                result.append(-1)
                
        return result