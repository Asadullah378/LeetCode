
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxc = max(candies)
        result = []

        for i in candies:
            if i+extraCandies >= maxc:
                result.append(True)
            else:
                result.append(False)

        return result