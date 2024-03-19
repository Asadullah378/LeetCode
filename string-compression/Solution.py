
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i=0

        while i<len(chars):

            if i+1 < len(chars) and chars[i][0] == chars[i+1]:
                chars[i] += chars[i+1]
                del chars[i+1]
            else:
                i+=1

        i = 0
        while i<len(chars):
            
            l = str(len(chars[i]))
            if l!="1":
                chars[i] = chars[i][0]

                for c in l:
                    chars.insert(i+1,c)
                    i+=1
            i+=1
