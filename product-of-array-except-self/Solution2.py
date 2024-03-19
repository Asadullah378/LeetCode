
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        prod_z = 1
        output = [0]*len(nums)
        zero = 0

        for i in range(len(nums)):
            
            if nums[i]==0:
                zero+=1
                prod_z *= 1
            else:
                prod_z *= nums[i]

            if zero>1:
                return output
            
            prod *= nums[i]
            
        for i in range(len(nums)):

            if nums[i]==0:
                output[i]=prod_z
            else:
                output[i]=prod//nums[i]

        return output
