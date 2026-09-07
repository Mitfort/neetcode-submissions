class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []

        for curr in asteroids:

            while st and st[-1] > 0 and curr < 0:
                diff = curr + st[-1]

                if diff < 0:
                    st.pop()
                elif diff > 0:
                    break
                else:
                    st.pop()
                    break

            else:
                st.append(curr)

        return st 
        ##############
        # st = []
        # idx:int = 1

        # st.append(asteroids[0])

        # while st and idx < len(asteroids):
        #     defender = st.pop()
        #     attacker = asteroids[idx]
        #     idx += 1
            
        #     if defender * attacker > 0:
        #         st.append(defender)
        #         st.append(attacker)
        #         continue

        #     if abs(defender) == abs(attacker):
        #         continue
            
        #     if abs(attacker) > abs(defender):
        #         st.append(attacker)
        #     else:
        #         st.append(defender)

        # res:List[int] = []

        # while st:
        #     res.append(st.pop())
        
        # return res[::-1]
        
            

            

            
            


