class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)-2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot > 0:
                    k -= 1
                elif tot < 0:
                    j += 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return list(ans)
