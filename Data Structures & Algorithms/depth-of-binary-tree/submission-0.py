# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxLength = self.BFS(root, 0, 0)
    
        return maxLength

    def BFS(self, node, length, maxLength):
        length += 1

        if length > maxLength: maxLength = length

        if node.left:
            maxLength = self.BFS(node.left, length, maxLength)
        
        if node.right:
            maxLength = self.BFS(node.right, length, maxLength)

        length -= 1

        return maxLength
        