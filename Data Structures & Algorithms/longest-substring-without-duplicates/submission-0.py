class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        j, length = 0, 0
        res = 0

        for i, char in enumerate(s):
            length += 1
            if char in seen:
                while char in seen:
                    length -= 1
                    del seen[s[j]]
                    j += 1
            seen[char] = i
            res = max(res, length)
        
        return res
