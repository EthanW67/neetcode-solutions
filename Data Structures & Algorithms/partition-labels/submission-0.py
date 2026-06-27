class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endFreq = {}
        for idx, val in enumerate(s):
            endFreq[val] = idx
        end = 0
        result = []
        value = 0
        for idx, char in enumerate(s):
            value += 1
            end = max(end, endFreq[char])
            if end == idx:
                result.append(value)
                value = 0
        return result