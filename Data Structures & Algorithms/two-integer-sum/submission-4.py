class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_pos = {}
        for i in range(len(nums)):
            if nums[i] in res_pos and i != res_pos[nums[i]]:
                return [res_pos[nums[i]], i]
            res_pos[target - nums[i]] = i            
