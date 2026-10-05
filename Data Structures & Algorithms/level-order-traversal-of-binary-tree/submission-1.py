# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res:List[List[int]] = []

        q = deque([]) 
        q.append(root)

        # BFS 
        while q:
            level:list = [] # Save values on the same level
            
            for i in range(len(q)): 
                node = q.popleft()

                if not node:
                    continue 
                
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if level:
                res.append(level)

        return res






