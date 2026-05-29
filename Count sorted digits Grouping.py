class Solution:
    def validGroups(self, s):
        # code here
        n = len(s)
        
        # dp[index][prev_sum] = number of ways
        dp = [[-1] * 901 for _ in range(n + 1)]
        
        def solve(index, prev_sum):
            # Reached end → one valid grouping
            if index == n:
                return 1
            
            if dp[index][prev_sum] != -1:
                return dp[index][prev_sum]
            
            ans = 0
            curr_sum = 0
            
            # Try every possible substring
            for j in range(index, n):
                curr_sum += int(s[j])
                
                # Valid only if non-decreasing
                if curr_sum >= prev_sum:
                    ans += solve(j + 1, curr_sum)
            
            dp[index][prev_sum] = ans
            return ans
        
        return solve(0, 0)
