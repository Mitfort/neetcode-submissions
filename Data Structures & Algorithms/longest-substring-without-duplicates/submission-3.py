class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen:int = 0
        chars = set()

        l:int = 0
        currLen:int = 0
        n:int = len(s)

        for r in range(n):
            char = s[r]

            while char in chars:
                chars.remove(s[l])
                l+=1
                currLen -= 1
            
            chars.add(s[r])
            currLen += 1

            if currLen > maxLen:
                maxLen = currLen
            
        return maxLen
            
            


                
