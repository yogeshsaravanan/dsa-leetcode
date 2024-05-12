class Solution:
    def isPalindrome(self, x: int) -> bool:
        # string conversion
        # if str(x)==str(x)[::-1]:
        #     return True
        # else:
        #     return False
        
        # without string Conversion
        X=0
        org =x
        while x>0:
            X= x%10 + X*10
            x=x//10
        if X==org:
            return True
        else:
            return False
        
