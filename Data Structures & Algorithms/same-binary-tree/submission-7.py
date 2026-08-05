# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame: bool = True
        
        if not p and not q:
            return True
        
        def DFS(node1,node2):
            if node1 and node2:
                if node1.val != node2.val:
                    self.isSame = False
                    return
            elif (node1 and not node2) or (not node1 and node2):
                self.isSame = False
                return
            
            if node1.left and node2.left:
                DFS(node1.left,node2.left)
            elif (node1.left and not node2.left) or (not node1.left and node2.left):
                self.isSame = False
                return
            
            if node1.right and node2.right:
                DFS(node1.right,node2.right)
            elif (node1.right and not node2.right) or (not node1.right and node2.right):
                self.isSame = False
                return

        DFS(p,q)
        
        return self.isSame



            
