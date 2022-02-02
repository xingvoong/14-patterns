"""
Given the root of a binary tree, return the zigzag level order traversal of its node's values. (i.e., from left to right, then right to left for the next level and alternate)

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- - 100 <= Node.val <= 100

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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()

    # 1 way of doing this is just get all the level
    # and then reverse it later
    # let see whether this will work

    def zigzagLevelOrder(self, root):
        def levelOrder(root):
            levels = []

            if not root:
                return levels

            # open a level
            def helper(node, level):
                if len(levels) == level:
                    levels.append([])

                levels[level].append(node.value)
                if node.left:
                    helper(node.left, level + 1)
                if node.right:
                    helper(node.right, level + 1)

            helper(root, 0)
            return levels

        levels = levelOrder(root)
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i] = levels[i][::-1]

        return levels


root = TreeNode(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.zigzagLevelOrder(root))

"""
complexity

Let N be the number of nodes in the tree
time: levelOrer +  1 for loop * reverse list

levelOrder: O(N), because I visit each node of the tree 1

loop and then reverse: O(log(N)) / 2 * 2
=> total runtime: O(N)

space: O(N)

"""
