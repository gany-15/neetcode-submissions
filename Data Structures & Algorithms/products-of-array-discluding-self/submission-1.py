class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suf = [1] * len(nums)
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = nums[i+1] * suf[i + 1]
        for i in range(len(nums)):
            ans[i] = pref[i] * suf[i]
        
        return ans
