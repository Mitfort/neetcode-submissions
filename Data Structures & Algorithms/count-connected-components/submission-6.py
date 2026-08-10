class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.counter:int = 0

        dic: dict[int,list[int]] = {i:[] for i in range(n)}

        for cur, nex in edges:
            dic[cur].append(nex)
            dic[nex].append(cur)

        visited = set()

        def dfs(node):
            if node in visited:
                return 

            nextList = dic[node]

            visited.add(node)

            for nex in nextList:
                if nex not in visited:
                    dfs(nex)

        for i in range(n):
            if i not in visited:
                dfs(i)
                self.counter += 1 

        return self.counter