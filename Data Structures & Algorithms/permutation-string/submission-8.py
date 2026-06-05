class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): 
            return False
        # left = 0
        # for right in range(len(s1) -1 , len(s2)):

        #     if ''.join(sorted(s1)) == ''.join(sorted(s2[left:right+1])):
        #         return True
        #     left += 1

        # return False 


        s1Freq = {}
        for i in range(len(s1)):
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
        s2Freq = {}
        left = 0
        for right in range(len(s2)):
            s2Freq[s2[right]] = 1 + s2Freq.get(s2[right], 0)
                
            if len(s1) < (right - left + 1):
                s2Freq[s2[left]] -= 1
                if s2Freq[s2[left]] == 0:
                    del s2Freq[s2[left]]
                left += 1

            if s2Freq == s1Freq:
                return True

        return False
            