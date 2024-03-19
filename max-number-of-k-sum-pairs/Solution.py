
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        temp = {}
        op = 0

        for i in range(len(nums)):
            t = str(k-nums[i])
            s = str(nums[i])

            if t in temp and temp[t]>0:
                temp[t]-=1
                op+=1
            elif s in temp:
                temp[s] +=1
            else:
                temp[s] = 1 

        return op


