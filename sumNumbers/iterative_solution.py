"""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
- For example, the root-to-left path 1->2->3 represents the number 123

Return the total sum of all root-to-leaf numbers.  Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

"""


def sumNumbers(root, TreeNode):
    root_to_leaf = 0
    stack = [(root, 0)]

    while stack:
        root, curr_number = stack.pop()
        if root is not None:
            # build up the number
            curr_number = curr_number * 10 + root.val
            # add the path number to root-to-leaf, update root-to-leaf sum
            if root.left is None and root.right is None:
                root_to_leaf += curr_number
            else:
                stack.append((root.right, curr_number))
                stack.append((root.left, curr_number))

    return root_to_leaf


"""
time: O(N) since one has to visit each node
space: O(H) to keep the stack, where H is a tree height

"""
