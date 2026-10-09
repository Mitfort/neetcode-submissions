# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.isValid:bool = True 
    
        def dfs(node,minimum,maximum):
            if not node:
                return 

            if not minimum < node.val < maximum:
                self.isValid = False
                return 

            dfs(node.left, minimum, node.val)
            dfs(node.right, node.val, maximum)

        dfs(root, float("-inf"), float("inf"))
            
        return self.isValid 