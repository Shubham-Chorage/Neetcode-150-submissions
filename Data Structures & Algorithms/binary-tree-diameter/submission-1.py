# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Diameter is sum of left and right nodes we need max of it so check depth
# at each and then sum left depth plus right then return the max depth

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def Depth(root):

            if not root:
                return 0

            ld = Depth(root.left)
            rd = Depth(root.right)

            self.diameter = max(self.diameter, ld + rd)

            return 1 + max(ld,rd)

        Depth(root)
        return self.diameter
