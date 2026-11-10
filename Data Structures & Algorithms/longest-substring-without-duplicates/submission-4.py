class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen:int = 0 
        window = defaultdict(int)
        length:int = 0
        l = 0

        for r in range(len(s)):
            c = s[r]

            while window[c]:
                window[s[l]] -= 1
                length -= 1
                l+=1

            window[c] += 1
            length += 1

            if length > maxLen:
                maxLen = length

        return maxLen
            
