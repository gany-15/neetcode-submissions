class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l, maxf, res = 0, 0, 0

        for r, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            maxf = max(maxf, d[char])

            while r - l + 1 - maxf > k:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
