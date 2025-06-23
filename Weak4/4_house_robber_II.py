class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            prev1 = prev2 = 0
            for num in houses:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))