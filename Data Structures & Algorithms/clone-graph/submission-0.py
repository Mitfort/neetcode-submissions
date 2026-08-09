"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        dic = {}
        dic[node] = Node(node.val)

        q = collections.deque([node])

        while q:
            curr = q.popleft()

            for Nnode in curr.neighbors:
                if Nnode not in dic:
                    dic[Nnode] = Node(Nnode.val)
                    q.append(Nnode)

                dic[curr].neighbors.append(dic[Nnode])


        return dic[node] 


