# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res=[]

        def preorder(root):
            if not root:
                return
            
            preorder(root.left)
            
            preorder(root.right)
            res.append(root.val)
        preorder(root)
        return res