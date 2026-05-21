class Solution:
    def isBitSet(self, n):
        # 0 should return False
        if n == 0:
            return False
        # Check if n is of the form 2^k - 1
        return (n & (n + 1)) == 0
