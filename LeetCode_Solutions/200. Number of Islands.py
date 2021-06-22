# Source : https://leetcode.com/problems/number-of-islands/
# Author : foxfromworld
# Date  : 22/06/2021
# Fifth attempt (BFS)

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    count = 0
    row, col = len(grid), len(grid[0])
    from collections import deque
    queue = deque([])
    for rw in range(row):
      for cl in range(col):
        if grid[rw][cl] == '1':
          count += 1
          grid[rw][cl] = '0'
          queue.append((rw, cl))
          while queue:
            r, c = queue.popleft()
            if r >= 1 and grid[r-1][c] == '1':
              queue.append((r-1, c))
              grid[r-1][c] = '0'
            if r < row-1 and grid[r+1][c] == '1':
              queue.append((r+1, c))
              grid[r+1][c] = '0'
            if c >= 1 and grid[r][c-1] == '1':
              queue.append((r, c-1)) 
              grid[r][c-1] = '0'           
            if c < col-1 and grid[r][c+1] == '1':
              queue.append((r, c+1))
              grid[r][c+1] = '0'
    return count

# Date  : 22/06/2021
# Fourth attempt (BFS)

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    count = 0
    for rw in range(row):
      for cl in range(col):
        if grid[rw][cl] == '1':
          count += 1
          from collections import deque
          queue = deque([(rw, cl)])
          grid[rw][cl] = '0'
          while queue:
            r, c = queue.popleft()
            for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
              if 0 <= adj_r < row and 0 <= adj_c < col and grid[adj_r][adj_c] == '1':
                grid[adj_r][adj_c] = '0'
                queue.append((adj_r, adj_c))
    return count 

# Date  : 22/06/2021
# Third attempt (BFS)

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          from collections import deque
          queue = deque([(rw, cl)])
          visit.add((rw, cl))
          while queue:
            r, c = queue.popleft()
            for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
              if 0 <= adj_r < row and 0 <= adj_c < col and grid[adj_r][adj_c] == '1' and (adj_r, adj_c) not in visit:
                visit.add((adj_r, adj_c))
                queue.append((adj_r, adj_c))
    return count  

# Date  : 19/06/2021
# Second attempt

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    def dfs(r, c):
      if (r, c) in visit or r < 0 or r >= row or c < 0  or c >= col or grid[r][c] == '0':
        return
      visit.add((r, c))
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          dfs(rw, cl)
    return count

# Date  : 19/06/2021
# First attempt (DFS)

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    def dfs(r, c):
      if (r, c) not in visit and grid[r][c] == '1':
        visit.add((r, c))
        for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
          if 0 <= adj_r < row and 0 <= adj_c < col:
            dfs(adj_r, adj_c)
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          dfs(rw, cl)
    return count
