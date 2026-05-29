class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = 0
            else:
                d1[s[i]] += 1
            
            if t[i] not in d2:
                d2[t[i]] = 0
            else:
                d2[t[i]] += 1
        
        if len(d1) != len(d2):
            return False
        
        for key in d1:
            if key not in d1 or key not in d2 or d1[key] != d2[key]:
                return False
        return True
