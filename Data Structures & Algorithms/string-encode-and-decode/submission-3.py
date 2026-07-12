class Solution:

    def encode(self, strs: List[str]) -> str:
        string = []
        for word in strs:
            string.append(str(len(word)) + "#" + word)
        return ''.join(string)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length             
            result.append(str(s[i:j]))
            i = j
        return result