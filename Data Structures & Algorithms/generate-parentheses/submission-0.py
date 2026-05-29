class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        st = ["("]

        def create(o, c):
            if o == c == n:
                ans.append("".join(st))
                return
            if o < n:
                st.append("(")
                create(o+1, c)
                st.pop()
            if c < o:
                st.append(")")
                create(o, c+1)
                st.pop()
        
        create(1, 0)
        return ans
