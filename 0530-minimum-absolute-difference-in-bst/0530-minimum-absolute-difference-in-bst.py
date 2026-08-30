# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def getMinimumDifference(self, root):
        self.prev=None
        self.mins=float('inf')

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            if self.prev and root :
                self.mins=min(self.mins,root.val-self.prev.val)
            self.prev=root
            inorder(root.right)
           

        inorder(root)
        return self.mins