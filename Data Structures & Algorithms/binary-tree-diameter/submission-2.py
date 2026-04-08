# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def Depth(node):

            if not node:
                return 0

            ld = Depth(node.left)
            rd = Depth(node.right)

            self.diameter = max(self.diameter, ld + rd)

            return 1 + max(ld,rd)
        
        Depth(root)

        return self.diameter

            