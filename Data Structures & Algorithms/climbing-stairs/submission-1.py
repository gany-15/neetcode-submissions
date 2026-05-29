class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0: 1}

        def helper(nn: int) -> int:
            if nn in dp:
                return dp[nn]
            elif nn >= 2:
                dp[nn] = helper(nn - 1) + helper(nn - 2)
            else:
                dp[nn] = helper(nn - 1)
            return dp[nn]
        
        return helper(n)
        