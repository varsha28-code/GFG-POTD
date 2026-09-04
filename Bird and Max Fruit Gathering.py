class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        class Solution:
        def maxFruits(self, arr, m):
            n = len(arr)
            # First window
            window_sum = sum(arr[:m])
            max_sum = window_sum
            # Slide the window
            for i in range(m, n + m - 1):
                window_sum -= arr[(i - m) % n]
                window_sum += arr[i % n]
                max_sum = max(max_sum, window_sum)
            return max_sum

