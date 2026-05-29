class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        p2 = cost[-1]
        p1 = min(cost[-2], cost[-2] + cost[-1])

        for i in range(len(cost) - 3, -1, -1):
            temp = p1
            p1 = cost[i] + min(p1, p2)
            p2 = temp
        
        return min(p1, p2)
