#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for index in range(rows)]
        result = False
        for index1 in range(rows):
            for index2 in range(cols):
                idx = 0
                if self.search(board, visited, word, index1, index2, idx):
                    return True
                
        return False
                
    def search(self,board: [[str]], visited: [[bool]], word: str, 
               index_row: int, index_column: int, index_char: int) -> bool:
        if index_char == len(word):
            return True
        rows = len(board)
        cols = len(board[0])
        if (index_row < 0 or index_column < 0 or index_row >= rows or index_column >= cols or
           visited[index_row][index_column] or word[index_char] != board[index_row][index_column]):
            return False
        visited[index_row][index_column] = True
        result = False
        result = (self.search(board, visited, word, index_row - 1, index_column, index_char + 1) or
                  self.search(board, visited, word, index_row + 1, index_column, index_char + 1) or
                  self.search(board, visited, word, index_row, index_column - 1, index_char + 1) or
                  self.search(board, visited, word, index_row, index_column + 1, index_char + 1))
        visited[index_row][index_column] = False
        return result


# In[4]:


a = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
b = "ABCCED"
test = Solution()
test.exist(a,b)


# In[ ]:




