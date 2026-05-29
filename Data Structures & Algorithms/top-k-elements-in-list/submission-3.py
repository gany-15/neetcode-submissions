class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        maxval = 0
        buckets = defaultdict(list)
        for key, value in d.items():
            if value > maxval:
                maxval = value
            buckets[value].append(key)
        
        ans = []
        while (len(ans) < k):
            while maxval not in buckets and maxval > 0:
                maxval -= 1
            ans = ans + buckets[maxval]
            maxval -= 1

        return ans