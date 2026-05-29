class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_pos = {}
        for i in range(len(nums)):
            res_pos[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in res_pos and i != res_pos[nums[i]]:
                return [i, res_pos[nums[i]]]
