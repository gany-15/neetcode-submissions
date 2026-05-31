class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0

        for num in numset:
            acc = 1
            curr = num
            if num - 1 not in numset:
                while curr + 1 in numset:
                    curr += 1
                    acc += 1
                maxlen = max(maxlen, acc)
        
        return maxlen
