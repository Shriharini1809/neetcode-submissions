# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left = 0
        right = 0
        balanced_left = True
        balanced_right = True

        
        

        if root.left is not None:
            left = self.height(root.left)
            balanced_left = self.isBalanced(root.left)
        if root.right is not None:
            right = self.height(root.right)
            balanced_right = self.isBalanced(root.right)
        
        if abs(left-right)<=1 and balanced_left and balanced_right:
            return True
        return False
        