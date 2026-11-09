class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        res = 0

        for n in nums:
            if not dct[n]:
                dct[n] = dct[n - 1] + dct[n + 1] + 1
                dct[n - dct[n - 1]] = dct[n]
                dct[n + dct[n + 1]] = dct[n]
                res = max(res,dct[n])

        return res


        # save = defaultdict(int)
        # save[nums[0]] = nums[0]

        # for n in nums[1:]:
        #     if save[n - 1] != -1:
        #         save[n - 1] = n
            
        #     elif save[n + 1] != -1:
        #         save[n] = save[n+1]

        #     else:
        #         save[n] = n 
        
        # maxLen:int = 0 
        # start:int = 0

        # for key,val in save.items():
        #     length = val - key + 1

        #     if length > maxLen:
        #         print(key,val)
        #         maxLen = length
        #         start = key

        # return maxLen
            

        