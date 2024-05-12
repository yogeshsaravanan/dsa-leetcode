class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        S=0
        prev='M'
        for i in s:
            if roman_dict[prev]<roman_dict[i]:
                t =roman_dict[i]-roman_dict[prev]
                S=t+S-roman_dict[prev]
            else:
                S=roman_dict[i]+S
            prev=i
        return S
        
