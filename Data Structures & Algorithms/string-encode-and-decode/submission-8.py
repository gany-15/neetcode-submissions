class Solution:
    def encode(self, strs: List[str]) -> str:
        s = '';
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        i, j = 0, 1
        strs = []

        while j < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            strs.append(s[j:j + length])
            i = j + length
            j = i + 1
        
        return strs
