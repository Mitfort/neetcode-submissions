# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        self.res:bool = True

        def dfs(node,minimum,maximum):
            if not node:
                return

            if  minimum < node.val < maximum:
                dfs(node.left,minimum,node.val)
            else:
                self.res = False 
                return
            
            if  minimum < node.val < maximum:
                dfs(node.right,node.val,maximum)
            else:
                self.res = False
                return
            

        dfs(root,float('-inf'),float('inf'))

        return self.res 

             
            
        