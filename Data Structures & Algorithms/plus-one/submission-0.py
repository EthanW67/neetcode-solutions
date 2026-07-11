class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        num = len(digits) - 1

        for num in range(len(digits)-1, -1,-1):
            
            digits[num] += 1
            if digits[num] < 10:
                return digits
            digits[num] = 0
        return [1]+ digits