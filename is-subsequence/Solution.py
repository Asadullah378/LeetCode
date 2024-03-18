// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        l = len(s)

        if l==0:
            return True

        curr=0

        for i in t:
            if i==s[curr]:
                curr+=1
            if curr==l:
                return True

       