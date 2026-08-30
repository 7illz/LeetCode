# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        self.prev=None
        self.mins=float('inf')

        def dfs(root):


            if not root:
                return 


            dfs(root.left)

            if root and self.prev :
                self.mins=min(self.mins,(root.val-self.prev.val))
            self.prev=root
            dfs(root.right)

            return 
        dfs(root)
        return self.mins

        