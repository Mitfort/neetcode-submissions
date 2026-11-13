class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = {}
        window = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have = 0
        need = len(count_t)

        minLen = float("inf")
        start, end = -1, -1

        l = 0

        for r in range(len(s)):
            c = s[r]

            if c in count_t:
                window[c] = window.get(c, 0) + 1

                if window[c] == count_t[c]:
                    have += 1

            while have == need:
                if r - l + 1 < minLen:
                    start = l
                    end = r
                    minLen = r - l + 1

                left_char = s[l]

                if left_char in count_t:
                    window[left_char] -= 1

                    if window[left_char] < count_t[left_char]:
                        have -= 1

                l += 1

        if start == -1:
            return ""

        return s[start:end + 1]