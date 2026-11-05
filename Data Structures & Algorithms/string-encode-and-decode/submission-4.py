class Solution:

    def encode(self, strs: List[str]) -> str:
        res:str = ""

        for s in strs:
            n:int = len(s)
            res += f"{n}.{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        idx:int = 0
        length:int = len(s)
        n = ""
        
        while idx < length:
            if s[idx] != '.':
                n += s[idx]
                idx += 1 
            else:
                goto = int(n)
                n = ""
                word = s[idx+1:idx+goto+1]
                res.append(word)
                idx+=goto+1

        return res
            

