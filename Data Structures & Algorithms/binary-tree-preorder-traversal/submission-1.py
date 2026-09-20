# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,list):
        if root is None:
            return list
        list.append(root.val)
        self.preorder(root.left,list)
        self.preorder(root.right,list)
        return list

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        result = self.preorder(root,list)
        return result