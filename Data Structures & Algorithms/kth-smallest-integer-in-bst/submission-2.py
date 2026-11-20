# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.res = root.val
        self.idx = 0

        def dfs(node):
            if not node:
                return 

            # We go to the smallest element (always max left)
            dfs(node.left)

            self.idx += 1

            if self.idx == k:
                self.res = node.val
                return 

            dfs(node.right)

        dfs(root)

        return self.res






