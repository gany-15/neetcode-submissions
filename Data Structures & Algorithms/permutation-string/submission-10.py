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

        i, j = 0, M - 1
        while j < N - 1:
            if m1 == m2:
                return True
            m2[ord(s2[i]) - ord('a')] -= 1
            i += 1
            j += 1
            m2[ord(s2[j]) - ord('a')] += 1
        
        return m1 == m2
