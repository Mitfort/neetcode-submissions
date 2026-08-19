class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        #print(intervals)

        prevStart, prevEnd = intervals[0][0], intervals[0][1]
        res = []
        
        for i in range(1, len(intervals)):
            currStart,currEnd = intervals[i][0],intervals[i][1]

            if currStart > prevEnd:
                res.append([prevStart,prevEnd])
                prevStart = currStart
                prevEnd = currEnd
                continue

            prevStart = min(currStart,prevStart)
            prevEnd = max(currEnd, prevEnd)


        res.append([prevStart,prevEnd])            

        return res