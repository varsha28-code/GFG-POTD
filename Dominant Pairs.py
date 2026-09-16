class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        mid = n // 2

        first = sorted(arr[:mid])
        second = sorted(arr[mid:])

        ans = 0
        j = 0

        for x in first:
            while j < mid and x >= 5 * second[j]:
                j += 1

            ans += j

        return ans
