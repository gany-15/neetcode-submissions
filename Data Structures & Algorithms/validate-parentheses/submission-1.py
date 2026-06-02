class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openSet = set(['(','[','{'])
        closeSet = set([')',']','}'])
        for c in s:
            if c in openSet:
                st.append(c)
            elif c in closeSet:
                if not len(st):
                    return False
                elif c == ')' and st[-1] == '(':
                    st.pop()
                elif c == ']' and st[-1] == '[':
                    st.pop()
                elif c == '}' and st[-1] == '{':
                    st.pop()
                else:
                    return False
            else:
                return False
        return len(st) == 0
