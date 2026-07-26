class Solution:
    def levelSort(self, arr):
        # code here
        n = len(arr)
        ans = []
        i = 0         
        level = 1      
        while i < n:
            curr = arr[i:min(i + level, n)]
            curr.sort()
            ans.append(curr)
            i += level
            level *= 2
        return ans
        
