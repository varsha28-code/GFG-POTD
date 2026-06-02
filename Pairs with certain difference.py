class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = dp[i - 1]
            if arr[i] - arr[i - 1] < k:
                take = arr[i] + arr[i - 1]
                if i >= 2:
                    take += dp[i - 2]
                dp[i] = max(dp[i], take)
        return dp[n - 1] if n > 0 else 0
