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

        self.DFS(root)

        return root
    

    def DFS(self, node: Optional[TreeNode]):
        copy = node.left
        node.left = node.right
        node.right = copy
        
        if node.left:
            self.DFS(node.left)
        
        if node.right:
            self.DFS(node.right)


