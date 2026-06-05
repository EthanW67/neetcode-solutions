class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = {}
        count = 0
        maxLen = 0 
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxLen = max(maxLen, freq[s[right]])
            while (right - left + 1) - maxLen > k:
                freq[s[left]] -= 1
                left += 1
            count = max(count, right - left + 1)

        return count 