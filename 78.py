#!/usr/bin/env python
# coding: utf-8

# In[7]:


import copy
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        if not nums:
            return []
        
        result = [[]]
        
        for value1 in nums:
            for index in range(len(result)):
                result.append(result[index] + [value1])
            
        return result


# In[8]:


test = Solution()
test.subsets([1,2,3])


# In[ ]:




