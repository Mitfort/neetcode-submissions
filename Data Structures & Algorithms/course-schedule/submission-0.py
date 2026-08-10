class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dic = {crs:[] for crs in range(numCourses)}

        visited = set()

        for crs,pre in prerequisites:
            dic[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False

            preList = dic[course]
            
            if not preList: return True

            visited.add(course)

            for pre in preList:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            dic[course] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True