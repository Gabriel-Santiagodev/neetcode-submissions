class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}
        for letter in s:
            if not letter in hashmap1:
                hashmap1[letter] = 1
            hashmap1[letter] += 1
        for letter in t:
            if not letter in hashmap2:
                hashmap2[letter] = 1
            hashmap2[letter] += 1
        if hashmap1 == hashmap2:
            return True
        return False

        
            

