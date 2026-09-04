class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if not word1:
            return word2

        if not word2:
            return word1
        
        res:str = ""
        idx1:int = 0
        idx2:int = 0

        swap:bool = False

        while idx1 < len(word1) and idx2 < len(word2):
            
            if swap: 
                res += word2[idx2]
                idx2 += 1
                swap = False 
            else:
                res += word1[idx1]
                idx1 += 1
                swap = True

        if idx1 < len(word1):
            res += word1[idx1:]
        
        if idx2 < len(word2):
            res += word2[idx2:]

        return res
