// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        temp = {}
        temp2 = {}
        for i in arr:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1

        for i in temp:

            if temp[i] in temp2:
                return False
            temp2[temp[i]] = 1

        return True
