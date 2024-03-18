// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        i = 0
        while i<len(flowerbed) and n>0:

            if flowerbed[i]==0 and (i-1<0 or flowerbed[i-1]==0) and (i+1>=len(flowerbed) or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n-=1
            
            i+=1
        
      
        return True if n<=0 else False
            