
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
    
        count=0
        pointer=0
        for i in range(len(nums)):
            
            if nums[i]!=0:
                if pointer!=i:
                    nums[pointer]=nums[i]
                    nums[i]=0
                pointer+=1

