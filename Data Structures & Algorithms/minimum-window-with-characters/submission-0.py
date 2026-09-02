class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l1:int = len(s)
        l2:int = len(t)

        if not l1 or not l2:
            return ""

        need:dict[str | int] = {}
        have:dict[str | int] = {}
        res = [-1,-1]
        resLen:int = float("inf")

        for i in range(l2):
            need[t[i]] = need.get(t[i],0) + 1

        l:int = 0
        haveLen:int = 0
        needLen:int = len(need)

        for r in range(l1):
            c = s[r]
            have[c] = have.get(c,0) + 1

            if c in need and have[c] == need[c]:
                haveLen += 1

            while haveLen == needLen:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                have[s[l]] -= 1

                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveLen -= 1
                
                l+=1

        l,r = res

        return s[l:r+1] if resLen != float("inf") else ""