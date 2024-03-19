
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        output = [0]*len(nums)
        zero = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
                output[i]=1
            else:
                zero+=1

        for i in range(len(nums)):

            if output[i]==1:
                if zero!=0:
                    nums[i]=0
                else:
                    nums[i] = prod//nums[i]

            elif zero==1:
                nums[i] = prod
            else:
                nums[i] = 0


        return nums
