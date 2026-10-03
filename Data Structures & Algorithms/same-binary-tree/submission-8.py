# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.isSame:bool = True

        def dfs(first,second):
            if not first and not second:
                return 

            if not first and second:
                self.isSame = False
                return 
            
            if first and not second:
                self.isSame = False
                return

            if first.val != second.val:
                self.isSame = False
                return

            dfs(first.left,second.left)
            dfs(first.right,second.right)

        dfs(p,q)

        return self.isSame