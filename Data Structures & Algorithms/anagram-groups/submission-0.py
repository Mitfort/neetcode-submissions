class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        res.append([strs[0]])

        for i in range(1, len(strs)):
            isSorted = False

            for j,arr in enumerate(res): 
                if sorted(strs[i]) == sorted(arr[0]):
                    res[j].append(strs[i])
                    isSorted = True
                    break
            
            if not isSorted:
                res.append([strs[i]])
    
        return res