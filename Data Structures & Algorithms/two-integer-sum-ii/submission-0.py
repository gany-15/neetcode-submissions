class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            m, n = numbers[i], numbers[j]
            if m + n > target:
                j -= 1
            elif m + n < target:
                i += 1
            else:
                return [i+1, j+1]
