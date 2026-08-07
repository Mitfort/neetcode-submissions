class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def DFS(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            DFS(i + 1)

            subset.pop()
            DFS(i+1)

        DFS(0)

        return res
        