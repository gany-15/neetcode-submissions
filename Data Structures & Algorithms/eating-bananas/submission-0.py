class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        
        while l <= r:
            mid = l + (r - l) // 2
            time = sum([math.ceil(piles[i] / mid) for i in range(len(piles))])
            if time <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
