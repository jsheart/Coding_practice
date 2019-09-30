
# coding: utf-8

# In[2]:


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#         return s
#         max_length = 0
#         start = -1
#         for index, value in enumerate(s):
#             even_length = -1
#             if index < len(s) - 1:
#                 even_length = self.check_palindrome(s, index, index + 1) 
#             odd_length = -1
#             odd_length = self.check_palindrome(s, index, index)           
            
#             if even_length > odd_length and even_length > max_length:
#                 max_length = even_length
#                 start = index - even_length // 2 + 1
#             if odd_length > even_length and odd_length > max_length:
#                 max_length = odd_length
#                 start = index - odd_length // 2
                
#         return s[start:(start + max_length)]    
    
#     def check_palindrome(self, s: str, left: int, right: int) -> int:
#         length = 0
#         while left > -1 and right < len(s):
            
#             if s[left] == s[right]:
#                 if length < right - left + 1:
#                     length = right - left +1
#                 left -= 1
#                 right += 1
#             else:
#                 if length < right - left -1:
#                     length = right - left -1
#                 break

#         return length
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [ [0] * len(s) for i in s ]
        start = 0
        max_length = 1
        for right in range(len(s)):
            dp[right][right] = True
            for left in range(right):
                dp[left][right] = (s[left] == s[right] and (right - left < 2 or dp[left + 1][right - 1]))
                if dp[left][right] and max_length < right - left + 1:
                    max_length = right - left + 1
                    start = left
        
        return s[start:(start + max_length)]
        
        


# In[3]:


test = Solution()
print(test.longestPalindrome("a"))


# In[4]:


print(test.longestPalindrome("ac"))


# In[99]:





# In[100]:





# In[101]:





# In[102]:





# In[103]:





# In[105]:




