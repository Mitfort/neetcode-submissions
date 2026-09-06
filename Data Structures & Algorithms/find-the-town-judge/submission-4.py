from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 1. Używamy set() zamiast list(), aby sprawdzanie 'in' trwało O(1)
        town: dict[int, set[int]] = {i: set() for i in range(1, n + 1)}

        for ai, bi in trust:
            town[ai].add(bi)
        
        # 2. Szukamy kandydatów (osób, które nikomu nie ufają)
        candidates = {person for person in town if not town[person]}

        # 3. Zamiast usuwać ze zbioru w trakcie pętli, tworzymy nową listę sędziów
        final_candidates = []
        for candidate in candidates:
            is_judge = True
            for person in town:
                if candidate == person:
                    continue
                if candidate not in town[person]:
                    is_judge = False
                    break
            
            if is_judge:
                final_candidates.append(candidate)
        
        if len(final_candidates) == 1:
            return final_candidates[0]

        return -1