class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n:int = len(nums)

        count:dict[int,int] = {}
        buckets:List[List[int]] = [[] for i in range(n+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n,cnt in count.items():
            buckets[cnt].append(n)

        res:List[int] = []
        taken:int = 0

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                if taken == k:
                    return res
                
                res.append(n)
                taken+=1

            if taken == k:
                return res

        return res



