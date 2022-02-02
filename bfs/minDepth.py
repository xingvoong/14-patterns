"""
Given a binary tree, find its mininum depth.

The mininum depth is the number of nodes along the shortest path from the root node down the nearest leaf node.

Note: a leaf is a node with no children

input: root = [3, 9, 20, null, null, 15, 7]
output: 2

example 2:
input: root = [2, null, 3, null, 4, null, 5, null 6]
output: 5

Constraints:
- the number of nodes in the tree is in the range [0, 10^5]
- -1000 <= Node.val <= 1000

"""


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

    def minDepth(root):
        return None
