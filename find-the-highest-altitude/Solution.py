
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curr = 0
        maxG = float('-inf')
        for i in gain:

            curr = curr+i
            if curr>maxG:
                maxG=curr
            

        return max(0,maxG)