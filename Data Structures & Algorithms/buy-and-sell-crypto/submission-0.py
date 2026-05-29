class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        i = 0
        profit = 0

        for j in range(1, len(prices)):
            diff = prices[j] - prices[i]
            if diff > 0 and profit < diff:
                profit = diff
            elif diff <= 0:
                i = j
        return profit

