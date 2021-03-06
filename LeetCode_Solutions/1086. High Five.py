# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 20/11/2020
# Second attempt 
import collections
class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:
    new_dict = collections.defaultdict(list)
    for item in items:
      new_dict[item[0]].append(item[1])
    return sorted([[key, sum(sorted(scores)[-5:])//5] for key, scores in new_dict.items()])
  
# Date  : 13/11/2020
# First attempt 
from typing import List
class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:
    items = sorted(items, reverse = True)    # Sort the list reversely
    cnt = sum = 0
    returnL = temp = []
    student = items[0][0]
    for i in range(len(items)):
      if student != items[i][0]: # Check if it's the new student. If it's the new student, reset variables and record the average score of the previous student.
        returnL.insert(0, [student, sum//5])
        student = items[i][0]
        temp = []
        cnt = sum = 0  
      if cnt<5 : # Sum the scores
        sum += items[i][1]
        cnt += 1     
    returnL.insert(0, [student, sum//5])
    return returnL
