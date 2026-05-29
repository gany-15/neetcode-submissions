class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [nums[0]]
        for i in range(1, len(nums)):
            fwd.append(nums[i] * fwd[i-1])
        
        bck = [1] * (len(nums) - 1) + [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            bck[i] = nums[i] * bck[i+1]
        
        ans = [1] * len(nums)
        ans[0] = bck[1]
        ans[-1] = fwd[-2]
        for i in range(1,len(nums) - 1):
            ans[i] = fwd[i-1] * bck[i+1]
        
        return ans
