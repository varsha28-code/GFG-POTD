''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        levels = []

        def dfs(node, level):
            if node is None:
                return

            # leaf node
            if node.left is None and node.right is None:
                levels.append(level)
                return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        levels.sort()

        count = 0

        for cost in levels:
            if cost > k:
                break

            k -= cost
            count += 1

        return count
        
