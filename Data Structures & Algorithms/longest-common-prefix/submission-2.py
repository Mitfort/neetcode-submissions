class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for st in strs:
                if i == len(st) or st[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]