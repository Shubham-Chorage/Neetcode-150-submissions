# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use DFS and call it recursively

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,curr_max):

            if not node:
                return 0
            
            good = 0

            if node.val >= curr_max:
                good = 1
                curr_max = node.val

            left = dfs(node.left, curr_max)
            right = dfs(node.right, curr_max)

            return good + left + right

        return dfs(root, float('-inf'))

        