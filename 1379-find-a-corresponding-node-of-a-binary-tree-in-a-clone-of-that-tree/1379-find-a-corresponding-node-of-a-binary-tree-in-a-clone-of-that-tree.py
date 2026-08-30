# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):

        def dfs(original,cloned):

           
                if not original :
                    return 
                if target is original :
                    return cloned

                left=dfs(original.left,cloned.left)
                if left:
                    return left

                right=dfs(original.right,cloned.right)
                if right:
                    return right 
                return 

            
        return dfs(original,cloned)



        


        