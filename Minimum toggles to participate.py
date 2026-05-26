class Solution:
    def minToggles(self, arr):
        total_zeros = arr.count(0)
        
        left_ones = 0
        right_zeros = total_zeros
        
        ans = right_zeros
        
        for num in arr:
            # Move current element from right part to left part
            if num == 0:
                right_zeros -= 1
            else:
                left_ones += 1
            
            ans = min(ans, left_ones + right_zeros)
        
        return ans
