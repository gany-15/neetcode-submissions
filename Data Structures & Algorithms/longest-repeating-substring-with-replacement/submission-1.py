class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxf, l, res = 0, 0, 0

        for r in range(len(s)):
            d[s[r]] += 1
            if d[s[r]] > maxf:
                maxf = d[s[r]]
            
            if r - l + 1 - maxf > k:
                d[s[l]] -= 1
                l += 1
                maxf = max(d.values())
            res = max(res, r - l + 1)
        
        return res
