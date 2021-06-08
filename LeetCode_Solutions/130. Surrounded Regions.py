# Source : https://leetcode.com/problems/surrounded-regions/
# Author : foxfromworld
# Date  : 08/06/2021
# First attempt (dfs)

class Solution(object):
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    row, col = len(board), len(board[0])
    def dfs(r, c):
      board[r][c] = '@' # When 'O' is visited, change it to '@'
      for dif_r, dif_c in (0, 1), (0, -1), (1, 0), (-1, 0):
        if (0 <= r+dif_r < row and 0 <= c+dif_c < col and 
            board[r+dif_r][c+dif_c] == 'O'):
          dfs(r+dif_r, c+dif_c)
    from itertools import product
    borders = (list(product([0, row - 1], range(col))) + 
          list(product(range(row), [0, col - 1])))
    for rw, cl in borders:
      if board[rw][cl] == 'O':
        dfs(rw, cl)
    for rw in range(row):
      for cl in range(col):
        if board[rw][cl] == '@':
          board[rw][cl] = 'O'
        elif board[rw][cl] == 'O':
          board[rw][cl] = 'X'
