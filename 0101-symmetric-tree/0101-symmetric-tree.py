# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def traverse(left,right):

            if left is None and right is None: 
                return True

            if left is None or right is None :
                return False

            if left.val!= right.val :
                return False

            return( left.val==right.val and traverse(left.left,right.right) and traverse(right.left,left.right))   


        return traverse(root.left,root.right)
        
