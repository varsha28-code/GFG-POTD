class Solution:
    def numOfWays(self, n, m):
        total = n * m
        all_positions = total * (total - 1)
        attacking = 0
        if n >= 2 and m >= 3:
            attacking += 4 * (n - 1) * (m - 2)
        if n >= 3 and m >= 2:
            attacking += 4 * (n - 2) * (m - 1)
        return all_positions - attacking
