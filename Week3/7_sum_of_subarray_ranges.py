from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        for i in range(n):
            maximum = minimum = nums[i]
            for j in range(i, n):
                maximum = max(maximum, nums[j])
                minimum = min(minimum, nums[j])
                result += maximum - minimum

        return result