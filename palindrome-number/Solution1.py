
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        
        if x==0:
            return True
        
        length = int(math.log(x, 10))

        for n in range(1, int((length+1)/2)+1):
 
            last_num = x%10
            first_num = (x // (10 ** (int(math.log(x, 10)) - n + 1)))%10
            x = x//10
            
            if first_num != last_num:
                return False

        return True

        