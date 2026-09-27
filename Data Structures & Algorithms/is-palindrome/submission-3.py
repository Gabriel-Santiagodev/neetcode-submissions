class Solution:
    def isPalindrome(self, s: str) -> bool:
        ctr = 0 
        s = s.replace(" ", "").lower()
        L = 0
        R = len(s) - 1

        if len(s) == 1:
            return True

        while L < len(s):
           
            if not s[R].isalnum() and R > 0:
                R -= 1
                continue
            if not s[L].isalnum():
                L +=1
                continue
            if s[L] != s[R]:
                return False
            L +=1
            R -=1
        return True
        

     