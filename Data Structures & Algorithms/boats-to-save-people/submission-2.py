class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l,r = 0, len(people) - 1
        n_boats:int = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            
            r-=1
            n_boats+=1

        return n_boats



        # people.sort(reverse=True)
        
        # n:int = len(people)
        # n_boats:int = 0 
        # away:List[bool] = [False] * n

        # l,r = 0,1
        # while l < n:
        #     if away[l]:
        #         l+=1
        #         r = l+1
        #         continue

        #     if r==n:
        #         l+=1
        #         r = l+1
        #         n_boats += 1
        #         continue

        #     if away[r]:
        #         r+=1
        #         continue 
    
        #     weight = people[l] + people[r]

        #     if weight > limit:
        #         r+=1
        #         continue
        #     else:
        #         away[l] = True
        #         away[r] = True
        #         n_boats += 1 
        #         l+=1
        #         r = l+1
                
        # return n_boats