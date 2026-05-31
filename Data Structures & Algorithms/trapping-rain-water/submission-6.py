class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N <= 1:
            return 0
        
        l, r = 0, N-1
        L, R = height[l], height[r]
        ans = 0

        while l < r:
            if L < R:
                l += 1
                L = max(L, height[l])
                ans += max(min(L, R) - height[l], 0)
            else:
                r -= 1
                R = max(R, height[r])
                ans += max(min(L, R) - height[r], 0)
        return ans
