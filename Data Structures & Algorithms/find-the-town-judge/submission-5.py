from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0] * (n+1)

        for ai,bi in trust:
            trust_score[ai] -= 1
            trust_score[bi] += 1
        
        for person in range(1,n+1):
            if trust_score[person] == n - 1:
                return person

        return -1