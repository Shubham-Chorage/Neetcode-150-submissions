# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def Depth(root):

            if not root:
                return 0

            ld = Depth(root.left)
            if ld == -1:
                return -1

            rd = Depth(root.right)
            if rd == -1:
                return -1

            if abs(ld-rd) > 1:
                return -1

            return 1 + max(ld,rd)

        return Depth(root) != -1