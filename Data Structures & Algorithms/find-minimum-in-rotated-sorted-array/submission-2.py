class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r]:
                res = min(nums[mid], res)
                r -= 1
            else:
                l += 1
        
        return res
