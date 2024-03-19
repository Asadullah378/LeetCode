
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        min1 = 2**31
        min2 = 2**31
        min3 = 2**31

        for i in range(len(nums)):

            if nums[i]<min1:
                min1 = nums[i]
            elif nums[i]<min2:
                if min1 != nums[i]:
                    min2 = nums[i]
            elif nums[i]<min3:
                if min1 != nums[i] and min2 != nums[i]:
                    min3 = nums[i]
    
    
        if min1 < min2 and min2 < min3 and min3 != 2**31:
            return True
        
        return False




