
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1)<=len(str2):
            s = str1
            b = str2
        else:
            s = str2
            b = str1

        for i in range(len(s),0,-1):
            pref = s[:i]
            
            rem_b = len(b)%len(pref)
            div_b = len(b)//len(pref)
            rem_s = len(s)%len(pref)
            div_s = len(s)//len(pref)

            if rem_b!=0 or rem_s!=0:
                continue
            
            elif pref*div_b == b and pref*div_s == s:
                return pref
        
        return ""


