class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort(key=lambda x:x[0])

        res:List[int] = []
        minHeap = []
        i,time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i+=1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, idx = heapq.heappop(minHeap)
                time += procTime

                res.append(idx)
        
        return res
            




