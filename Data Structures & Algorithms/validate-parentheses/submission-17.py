class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closing = {')': '(', '}': '{', ']':'['}

        for char in s:
            if char in closing:
                if not st or st[-1] != closing[char]:
                    return False
                st.pop()
            else:
                st.append(char)

        return not st