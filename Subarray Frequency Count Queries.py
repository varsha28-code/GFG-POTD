from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def freqInRange(self, arr, queries):
        pos = defaultdict(list)

        for i, num in enumerate(arr):
            pos[num].append(i)

        ans = []

        for l, r, x in queries:
            if x not in pos:
                ans.append(0)
                continue

            left = bisect_left(pos[x], l)
            right = bisect_right(pos[x], r)

            ans.append(right - left)

        return ans
