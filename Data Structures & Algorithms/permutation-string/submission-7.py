class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): 
            return False
        
        print(''.join(sorted(s2)))

        left = 0
        for right in range(len(s1) -1 , len(s2)):

            if ''.join(sorted(s1)) == ''.join(sorted(s2[left:right+1])):
                return True
            left += 1

        return False 

