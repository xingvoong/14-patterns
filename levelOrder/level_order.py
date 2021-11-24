'''
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e, from left to right, level by level)

example:
input: root = [3, 9, 20, null, null, 15, 7]
output: [[3], [9, 20], [15, 7]]

example 2:
input: root = [1]
output: [[1]]

example 3:
input: root = []
output: []
'''
# definition for a binary tree node
# class TreeNode(object):
#   def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(root):
  """
  :type root: TreeNode
  :rtype: List[List[int]]
  """