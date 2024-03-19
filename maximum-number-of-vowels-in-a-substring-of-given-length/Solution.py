
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = 0
        max = -1
        vowels = ['a','e','i','o','u']
  
        for i in range(len(s)):

            if s[i] in vowels:
                vowel+=1
            
            if i>=k-1:

                if vowel>max:
                    max=vowel
                if s[i-k+1] in vowels:
                    vowel-=1

        return max

