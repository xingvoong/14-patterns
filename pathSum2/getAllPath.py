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
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def getPaths(self, root):
        paths = []

        def helper(root, path):
            if root:
                path.append(root.value)

                # if the node is a leaf
                if not root.left and not root.right:
                    paths.append(path)

                else:
                    helper(root.left, path.copy())
                    helper(root.right, path.copy())

        helper(root, [])
        return paths

    def pathSum(self, root):
        toReturn = 0

        def helper(root, current_val):
            nonlocal toReturn
            if root:
                current_val = current_val * 10 + root.value
                if root.left == None and root.right == None:
                    toReturn += current_val
                if root.left != None:
                    helper(root.left, current_val)
                if root.right != None:
                    helper(root.right, current_val)

        helper(root, 0)
        return toReturn


root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.PrintTree()
# allPath = [[27, 14, 10], [27, 14, 19], [27, 35, 31], [27, 35, 42]]
print(root.getPaths(root))
print(root.pathSum(root))
