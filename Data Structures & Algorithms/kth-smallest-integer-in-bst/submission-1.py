# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0         

        # Go max to the left 
        # While idx < k increment 
        # Search left,parent,right
        self.smallest:int = 0
        self.k = k 

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.k -= 1

            if self.k == 0: 
                self.smallest = node.val
                return
            
            dfs(node.right)

        dfs(root)

        return self.smallest 



