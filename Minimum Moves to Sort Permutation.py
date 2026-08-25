class Solution:
    def minMoves(self, arr):
        """code here"""
        n = len(arr)

        # Store position of every value
        pos = [0] * (n + 1)

        for i in range(n):
            pos[arr[i]] = i

        longest = 1

        # Try every starting value
        for start in range(1, n + 1):
            length = 1

            # Try extending the sequence
            for x in range(start, n):
                if pos[x] < pos[x + 1]:
                    length += 1
                else:
                    break

            longest = max(longest, length)

        return n - longest
