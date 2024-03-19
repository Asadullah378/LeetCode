
class Solution:

    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        li = list(s)

        i = 0
        j = len(s)-1

        while i<=j:

            if li[i] in vowels and li[j] in vowels:
                li[i],li[j] = li[j],li[i]
                i+=1
                j-=1
            else:   
                if li[i] not in vowels:
                    i+=1
                if li[j] not in vowels:
                    j-=1   

        return "".join(li)   



        

