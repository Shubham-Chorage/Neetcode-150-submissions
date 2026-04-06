# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We will check if the nodes are equal at any point of time. Till then we keep going right or left

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True
        
        leftSide = self.isSubtree(root.left,subRoot)
        rightSide = self.isSubtree(root.right,subRoot)

        return leftSide or rightSide

    def isSameTree(self,p,q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        leftTree = self.isSameTree(p.left,q.left)
        rightTree = self.isSameTree(p.right,q.right)

        return True if leftTree and rightTree else False
        


