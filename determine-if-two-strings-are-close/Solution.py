class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        w1 = set(word1)
        w2 = set(word2)

        if w1!=w2:
            return False

        s1 = sorted([word1.count(c) for c in w1])
        s2 = sorted([word2.count(c) for c in w2])

        return s1==s2
