class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways:List[int] = [1] * n

        for i in range(1,m):
            for j in range(1,n):
                ways[j] += ways[j-1]
            
        return ways[-1]