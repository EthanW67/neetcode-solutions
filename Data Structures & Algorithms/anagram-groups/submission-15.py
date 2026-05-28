class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            sortWord = ''.join(sorted(word))
            result[sortWord].append(word)
        return list(result.values())