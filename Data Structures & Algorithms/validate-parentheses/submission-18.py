class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closing = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if c in closing:
                if st and st[-1] == closing[c]:
                    st.pop()
                else:
                    return False 
            else:
                st.append(c)
            
        return True if not st else False 

