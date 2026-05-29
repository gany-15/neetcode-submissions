class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        ans = [1] * n

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i+1] * suf[i + 1]
        for i in range(n):
            ans[i] = pref[i] * suf[i]
        
        return ans
