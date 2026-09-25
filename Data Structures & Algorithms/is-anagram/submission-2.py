class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for c in s: 
            s_count[c] = s_count.get(c,0) + 1
        
        for c in t: 
            t_count[c] = t_count.get(c,0) + 1

        return s_count == t_count