# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
        
#         substring=[]
#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 substring.append(s[i:j])
                
#         print(substring)
        
#         palindrome_list=[]
#         substring_list_2=[]
        
#         for s in substring:
            
#             if s == s[::-1] :
#                 substring_list_2.append(s)
                
#         print(substring_list_2)
        
#         palindrome_str=[]
        
#         for i in range(len(substring_list_2)):
#             for j in range(i+1,len(substring_list_2)):
#                 i,j
            
#         return substring_list_2
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
                
        
