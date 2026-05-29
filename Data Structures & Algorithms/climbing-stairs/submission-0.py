class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(nn: int) -> int:
            if nn == 0:
                return 1
            if nn >= 2:
                return helper(nn - 1) + helper(nn - 2)
            else:
                return helper(nn - 1)
        
        return helper(n)
        