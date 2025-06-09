from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final = 0

        for num in nums:
            final ^= num
        return final