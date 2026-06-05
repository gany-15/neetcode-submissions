class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if matrix[mid][0] > target:
            mid -= 1

        l, r, m = 0, len(matrix[0]) - 1, mid

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
