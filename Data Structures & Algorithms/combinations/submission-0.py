class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(val, curr):
            if len(curr) == k:
                res.append(list(curr))
                return
            
            for i in range(val,n+1):
                curr.append(i)
                
                backtrack(i+1,curr)

                curr.pop()
            
        
        
        backtrack(1,[])
            
        return list(res)


