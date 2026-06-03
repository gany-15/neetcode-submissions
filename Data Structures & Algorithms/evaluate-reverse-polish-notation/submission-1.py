class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+','-','*','/'])
        st = []

        def resultant(n1, n2, op):
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2
            if op == '*':
                return n1 * n2
            if op == '/':
                return int(n1 / n2)
        
        for tok in tokens:
            if tok not in ops:
                st.append(int(tok))
            else:
                n2 = st.pop()
                n1 = st.pop()
                
                st.append(resultant(n1, n2, tok))
        
        return st[-1]
