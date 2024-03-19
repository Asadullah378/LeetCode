
class Solution:

    def reverseVowels(self, s: str) -> str:
        
        length = len(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        res = ''
        res2 = ''

        temp = []
        for i in s:

            if i in vowels:
                temp.append(i)
                res+='a'
            else:
                res+=i

        j=len(temp)-1
        for i in res:

            if i == 'a':
                res2+=temp[j]
                j-=1
            else:
                res2+=i

        return res2

