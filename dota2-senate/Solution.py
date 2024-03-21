class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        queue = list(senate)
        D = 0
        R = 0

        while "R" in queue and "D" in queue:

            element = queue.pop(0)
            if element=='D':
                if D==0:
                    queue.append('D')
                    R+=1
                else:
                    D-=1
            else:
                if R==0:
                    queue.append('R')
                    D+=1
                else:
                    R-=1

        return 'Radiant' if queue.pop(0)=='R' else "Dire"
            

