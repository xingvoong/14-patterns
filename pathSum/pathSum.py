'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children

I: root of a tree, an integer, which is the target sum
O: boolean, whether a path sum to the given target
C:
E: root is None
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

    def getPaths(self, root):
      paths = []
      def helper(root, path):
        if root:
          path.append(root.value)
          if not root.left and not root.right:
            paths.append(path)
          if root.left:
            helper(root.left, path.copy())
          if root.right:
            helper(root.right, path.copy())
      helper(root, [])
      return paths

    def hasPathSum(self, root, targetSum):
      paths = self.getPaths(root)
      sumPaths = []
      for path in paths:
        sumPaths.append(sum(path))

      if targetSum in sumPaths:
        return True
      return False

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.PrintTree()
# allPath = [[27, 14, 10], [27, 14, 19], [27, 35, 31], [27, 35, 42]]
print(root.hasPathSum(root, 51))
