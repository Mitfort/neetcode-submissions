class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        idx = 0
        res = 0

        while idx < len(operations):
            if operations[idx] == '+':
                scores.append(scores[-1] + scores[-2])
            elif operations[idx] == 'D':
                scores.append(2 * scores[-1])
            elif operations[idx] == 'C':
                scores.pop()
            else:
                scores.append(int(operations[idx]))

            idx += 1
        
        for score in scores:
            res += int(score)

        return res
