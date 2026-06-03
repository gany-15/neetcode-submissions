class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(st) and temp > st[-1][1]:
                j, _ = st.pop()
                res[j] = i - j
            st.append((i, temp))
        
        return res

