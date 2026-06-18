class Solution:
    def findCoverage(self, mat):
        n = len(mat)
        m = len(mat[0])

        total = 0

        for i in range(n):
            for j in range(m):

                if mat[i][j] == 0:

                    # Left
                    for c in range(j - 1, -1, -1):
                        if mat[i][c] == 1:
                            total += 1
                            break

                    # Right
                    for c in range(j + 1, m):
                        if mat[i][c] == 1:
                            total += 1
                            break

                    # Up
                    for r in range(i - 1, -1, -1):
                        if mat[r][j] == 1:
                            total += 1
                            break

                    # Down
                    for r in range(i + 1, n):
                        if mat[r][j] == 1:
                            total += 1
                            break

        return total
