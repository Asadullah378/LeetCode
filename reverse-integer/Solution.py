// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        
        n = 0
        neg = False
        if x<0:
            x = -1*x
            neg = True

        while x!=0:

            n = n*10 + x%10
            x = x//10

        if n > ((2**31)-1) or n < ((-2)**31):
            return 0
        if neg:
            return -1*n
        else:
            return n