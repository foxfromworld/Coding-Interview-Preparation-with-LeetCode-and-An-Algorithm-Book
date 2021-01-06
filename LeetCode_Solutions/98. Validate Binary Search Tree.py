# Source : https://leetcode.com/problems/validate-binary-search-tree/
# Author : foxfromworld
# Date  : 05/01/2021
# First attempt 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """    
    def validate(node,left,right):
      if not node: return True
      if not left < node.val < right:
        return False
      return validate(node.left, left, node.val) and validate(node.right, node.val,right)
    return validate(root, float('-inf'), float('inf'))
