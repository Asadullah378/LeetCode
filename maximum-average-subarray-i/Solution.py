
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum = 0
        max = float('-inf')

        for i in range(len(nums)+1):

            if i>=k:
                print(sum)
                avg = sum/k
                if avg > max:
                    max = avg
                sum -= nums[i-k]
            
            if i<len(nums):
                sum += nums[i]

        return max



