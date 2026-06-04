class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char = set()
        left = 0 
        maxLength = 0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])

            maxLength = max(maxLength, right - left + 1)



        return maxLength
