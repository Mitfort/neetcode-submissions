class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s:dict[str,int] = {}
        counter_t:dict[str,int] = {}
 
        for c in s:
            counter_s[c] = counter_s.get(c,0) + 1 
        
        for c in t: 
            counter_t[c] = counter_t.get(c,0) + 1

        if counter_s == counter_t: 
            return True

        return False

