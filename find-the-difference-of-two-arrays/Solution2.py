// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        out = []
        set1 = set(nums1)
        set2 = set(nums2)

        out.append(list(set1-set2))
        out.append(list(set2-set1))
  
        return out