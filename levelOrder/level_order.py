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
  levels = []
  if not root:
    return levels

  def helper(node, level):
    # start the current level
    if len(levels) == level:
      levels.append([])

    # append the current node value
    levels[level].append(node.val)

    # process child nodes for the next level
    if node.left:
      helper(node.left, level + 1)
    if node.right:
      helper(node.right, level + 1)

  helper(root, 0)
  return levels

'''
Complexity Analysis
time: O(N), visit each node once
space: O(N), to keep the output structure which contains N ndoe values

'''

'''
Algo
- if the length of result is equal to the current tree level, create a new level for result.
- append the value of the current node
- if left node is not null, recursive on the left
- if right node is not null, recursive on the right.
- call the helper function on level 0

'''