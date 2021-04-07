# Source : https://leetcode.com/problems/rectangle-overlap/
# Author : foxfromworld
# Date  : 07/04/2021
# First attempt

class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    if rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
      rec2[0] == rec2[2] or rec2[1] == rec2[3]:
      return False # check if it's a line
    return rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec1[0] < rec2[2] and rec1[1] < rec2[3]
