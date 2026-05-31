class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        vol = 0

        while (i < j):
            curr = min(heights[i], heights[j]) * (j - i)
            vol = max(curr, vol)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return vol
