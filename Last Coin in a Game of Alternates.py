class Solution:
    def findLastCoin(self, arr):
        i = 0
        j = len(arr) - 1

        # Continue until one coin remains
        while i < j:
            # Remove the larger coin
            if arr[i] >= arr[j]:
                i += 1
            else:
                j -= 1

        return arr[i]
