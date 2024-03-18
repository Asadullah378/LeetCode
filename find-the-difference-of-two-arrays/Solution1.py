// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        out = [[],[]]
        
        for i in nums1:
            if i not in nums2 and i not in out[0]:
                out[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in out[1]:
                out[1].append(i)

        return out