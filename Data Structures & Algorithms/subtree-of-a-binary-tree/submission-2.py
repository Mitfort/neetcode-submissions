# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Convert both trees into strings
        # Then search for a substring 
        def buildString(node):
            if not node: 
                return "#"

            s:str = str(node.val)

            return "^" + s + buildString(node.left) + buildString(node.right)

        s1:str = buildString(root)
        s2:str = buildString(subRoot)

        print(s1,s2)

        return s2 in s1

