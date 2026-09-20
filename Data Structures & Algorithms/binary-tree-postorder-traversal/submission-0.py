# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,list):
        if root is None:
            return list
        self.postorder(root.left,list)
        self.postorder(root.right,list)
        list.append(root.val)
        return list

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        result = self.postorder(root,list)
        return result