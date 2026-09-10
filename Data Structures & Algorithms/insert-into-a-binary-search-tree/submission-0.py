# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)

        node = root

        while True:
            if val > node.val:
                if node.right == None:
                    node.right = TreeNode(val)
                    break 

                node = node.right
            elif val < node.val:
                if node.left == None:
                    node.left = TreeNode(val)
                    break
                
                node = node.left

        return root