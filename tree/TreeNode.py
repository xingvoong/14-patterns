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

  # print tree
  # visit the left
  # print the node val
  # visit the right
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.value)
    if self.right:
      self.right.PrintTree()

  # in-order traversal, left, node, right
  # create an empty list,
  # add left node first followed by the root or parent node

  def inorderTraversal(self, root):
    res = []
    if root:
      res = self.inorderTraversal(root.left)
      res.append(root.value)
      res += self.inorderTraversal(root.right)

    return res



root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
