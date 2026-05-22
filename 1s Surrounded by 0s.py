from collections import deque
class Solution:
    def cntOnes(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        q = deque()
        # Add all boundary 1's to queue
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # BFS to remove all connected boundary 1's
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        # Count remaining 1's
        count = 0
        for i in range(n):
            for j in range(m):
                count += grid[i][j]
        return count
