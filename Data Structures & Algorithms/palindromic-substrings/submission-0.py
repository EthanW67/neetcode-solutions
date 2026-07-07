class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.countPali(s, i, i)
            result += self.countPali(s, i, i + 1)
        return result
    def countPali(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result

        # for i in range(len(s)):
        #     left, right = i, i
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         result += 1
        #         left -= 1
        #         right += 1

        #     left, right = i, i + 1
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         result += 1
        #         left -= 1
        #         right += 1
        # return result