class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        frequencies = {}

        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1
        for char in t:
            if char not in frequencies:
                return False
            frequencies[char] -= 1

            if frequencies.get(char) < 0:
                return False
                
        return True 
        
            

