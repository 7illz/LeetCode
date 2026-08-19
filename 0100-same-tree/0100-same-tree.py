# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is not None and q is not None:
            if p.val!=q.val:
                return False

                
        elif p is None and q is not None:
            return False
            
        elif p is not None and q is None:
            return False
        elif p is None and q is None:
            return True
        
        left=self.isSameTree(p.left,q.left)
        if left==False:
            return False
        right=self.isSameTree(p.right,q.right)
        if right==False:
            return False
        return True

