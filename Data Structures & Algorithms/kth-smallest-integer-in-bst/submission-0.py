# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.kth = 0
        self.found = False

        def dfs(node):
            if self.found:
                return 

            if node.left:
                dfs(node.left)

            self.counter+=1

            if self.counter == k:
                self.kth = node.val
                self.found = True
                return

            if node.right:
                dfs(node.right)

        
        dfs(root)

        return self.kth