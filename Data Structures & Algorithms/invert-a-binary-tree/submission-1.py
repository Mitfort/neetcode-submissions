# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        self.BFS(root)

        return root
    

    def BFS(self, node: Optional[TreeNode]):
        copy = node.left
        node.left = node.right
        node.right = copy
        
        if node.left:
            self.BFS(node.left)
        
        if node.right:
            self.BFS(node.right)


