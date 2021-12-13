'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
the sum of the node values in the path equals targetSum.  Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children

Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], target sum = 22
Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1, 2, 3], targetSum = 5
Output: []

Example 3:
Input: root = [1, 2], targetSum = 0
Output: []

'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert into a binary tree
    # recursively go to the leaf so that I can add something.
    def insert(self, value):
        # if the node is there with a value already
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        # if the node is there but with no value
        else:
            self.value = value

    # def recurseTree(self, node, remainingSum, pathNodes, pathsList):
    #   if not node:
    #     return

    #   # add the current node to the path's list
    #   pathNodes.append(node.value)

    #   # check if the current node is a leaf and also, if it
    #   # equals our remaining sum.  if it does, we add the path to our list of paths
    #   if remainingSum == node.value and not node.left and not node.right:
    #     pathsList.append(list(pathNodes))
    #   else:
    #     # else, we will recurse on the left and right right children
    #     self.recurseTree(node.left, remainingSum - node.value, pathNodes, pathsList)
    #     self.recurseTree(node.right, remainingSum - node.value, pathNodes, pathsList)

    #   # we need to pop the node once we are done processing all of it's subtrees.
    #   # subTrees
    #   pathNodes.pop()


    def pathSum(self, root, targetSum):
      toReturn = []
      def helper(root, targetSum, path):
        nonlocal toReturn
        if root:
          path.append(root.value)
          if targetSum== root.value and not root.left and not root.right:
            toReturn.append(list(path))
          else:
            # don't make a copy every time, only make a copy when we append
            helper(root.left, targetSum - root.value, path)
            helper(root.right, targetSum - root.value, path)
          # we need to pop node once we are done processing all of it's subtree.
          path.pop()
      helper(root, targetSum, [])
      return toReturn

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.pathSum(root, 51))

'''
Time:
- O(N) to visit all the node, O(N) to copy list(path)
=> O(N^2)

Space:
- O(N) for additional space to store path
- or O(N) if counts the result space

'''
