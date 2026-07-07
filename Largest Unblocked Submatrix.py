class Solution:
    def largestArea(self, n, m, arr):
        # code here
        blockedRows = []
        blockedCols = []

        for r, c in arr:
            blockedRows.append(r)
            blockedCols.append(c)

        blockedRows.sort()
        blockedCols.sort()

        def maxGap(blocked, limit):
            prev = 0
            ans = 0

            for x in blocked:
                ans = max(ans, x - prev - 1)
                prev = x

            ans = max(ans, limit - prev)
            return ans

        maxRows = maxGap(blockedRows, n)
        maxCols = maxGap(blockedCols, m)

        return maxRows * maxCols
