# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False

        def dfs(node,subNode):
            if not node and not subNode:
                return True 

            if not node or not subNode:
                return False

            if node.val == subNode.val:
                return dfs(node.left,subNode.left) and dfs(node.right, subNode.right)
            
            return False
        
        if dfs(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)