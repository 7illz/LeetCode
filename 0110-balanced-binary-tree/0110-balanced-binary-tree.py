# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):

        def dfs(root):

            if not root:
                return [True,0]

            left = dfs(root.left )
            right = dfs(root.right)
            if abs(left[1] - right[1]) > 1:
                return [False,0]

            return  (left[0] and right[0] ,max(left[1], right[1]) + 1)

        return dfs(root)[0] 
