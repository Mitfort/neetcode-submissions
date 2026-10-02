# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.maxLen:int = 0

        def dfs(node,length):
            if not node:
                return 

            length += 1

            if length > self.maxLen:
                self.maxLen = length

            dfs(node.left, length)
            dfs(node.right, length)

        dfs(root,0)

        return self.maxLen