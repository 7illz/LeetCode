# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):


            if not root1 and not root2: 
                return 

            if not root1 and root2:
                var=0
                car=root2.val
                ki=None
                ka=None
                box=root2.left
                pox=root2.right

            if root1 and not root2:
                car=0
                var=root1.val
                ki=root1.left
                ka=root1.right
                box=None
                pox=None

            if root1 and root2:
                    var=root1.val
                    car=root2.val
                    ki=root1.left
                    ka=root1.right
                    box=root2.left
                    pox=root2.right

            root=TreeNode(var+car)


            root.left=self.mergeTrees(ki,box)




            root.right=self.mergeTrees(ka,pox)
            return root