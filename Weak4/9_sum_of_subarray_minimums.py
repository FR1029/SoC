class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        dp = [0] * n
        result = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev = stack[-1]
                dp[i] = dp[prev] + arr[i] * (i - prev)
            else:
                dp[i] = arr[i] * (i + 1)
            stack.append(i)
            result = (result + dp[i]) % MOD
            
        return result