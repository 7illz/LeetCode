# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def maxDepth(self, root):

        def traverse(root, lvl):
            lvl += 1

            if not root:
                return lvl - 1

            left = traverse(root.left, lvl)
            right = traverse(root.right, lvl)

            return max(left, right)

        return traverse(root, 0)
        