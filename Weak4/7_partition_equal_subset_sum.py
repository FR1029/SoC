class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0 :
            return False
        
        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                notTake = dp[i - 1][j]
                take = False
                
                if nums[i - 1] <= j:
                    take = dp[i - 1][j - nums[i - 1]]
                dp[i][j] = take or notTake
        
        return dp[n][target]