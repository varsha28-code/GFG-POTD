class Solution:
    def processQueries(self, arr, queries):
        # code here
        n = len(arr)

        # inc[i] = farthest index reachable from i
        # while array is non-decreasing
        inc = [0] * n
        inc[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i

        # dec[i] = leftmost index of current
        # non-increasing segment
        dec = [0] * n
        dec[0] = 0

        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                dec[i] = dec[i - 1]
            else:
                dec[i] = i

        ans = []

        for l, r in queries:
            ans.append(dec[r] <= inc[l])

        return ans
