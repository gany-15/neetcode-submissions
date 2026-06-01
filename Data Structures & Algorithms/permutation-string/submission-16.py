class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)

        if M > N:
            return False

        m1 = [0] * 26
        m2 = [0] * 26
        for i in range(M):
            m1[ord(s1[i]) - ord('a')] += 1
            m2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if m1[i] == m2[i]:
                matches += 1

        i, j = 0, M - 1
        while j < N:
            if matches == 26:
                return True
            elif j == N - 1:
                return matches == 26
            
            matches -= 1 if m2[ord(s2[i]) - ord('a')] == m1[ord(s2[i]) - ord('a')] else 0
            m2[ord(s2[i]) - ord('a')] -= 1
            matches += 1 if m2[ord(s2[i]) - ord('a')] == m1[ord(s2[i]) - ord('a')] else 0
            i += 1
            j += 1
            matches -= 1 if m2[ord(s2[j]) - ord('a')] == m1[ord(s2[j]) - ord('a')] else 0
            m2[ord(s2[j]) - ord('a')] += 1
            matches += 1 if m2[ord(s2[j]) - ord('a')] == m1[ord(s2[j]) - ord('a')] else 0
        
        return matches == 26
