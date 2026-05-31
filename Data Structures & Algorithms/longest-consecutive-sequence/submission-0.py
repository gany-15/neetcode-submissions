class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        lcs = {}
        maxlen = 0

        for num in numset:
            acc = 1
            curr = num
            if num - 1 in lcs:
                lcs[num] = lcs[num - 1] - 1
            else:
                while curr + 1 in numset:
                    curr += 1
                    acc += 1
                lcs[num] = acc
                if maxlen < lcs[num]:
                    maxlen = lcs[num]
        
        return maxlen
