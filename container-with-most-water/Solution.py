class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height)-1
        max = -1

        while start<end:

            if height[start]<=height[end]:
                area = (end-start)*height[start]
                start+=1
            else:
                area = (end-start)*height[end]
                end-=1

            if area>max:
                max=area

        return max


