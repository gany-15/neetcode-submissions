class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        j = 0
        res = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= j:
                j = seen[char] + 1
            seen[char] = i
            res = max(res, i - j + 1)
        
        return res
