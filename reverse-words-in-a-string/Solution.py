
class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        words = words[::-1]
        res = ""

        for i in range(len(words)):

            res+=words[i]

            if i+1 < len(words):
                res+=" "

        return res


        



