"""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.

For example, the root-to-leat path 1 -> 2 -> 3 represents the number 123

return the total sum of all root-to-leaf numbers.  Test cases are generated so that the answer will fit in a 32-bit integer

A leaf node is a node with no children.

I: a root of a tree
O: an integer
C:
- the number of nodes in the tree is in the range [1, 1000]
- 0 <= Node.val <= 9
- The death of the tree will node exceed 10.
E:

I need to do it in preorder (root, left, right)
"""


def sumNumber(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    result = 0

    # use preorder traversal to find the sum
    def findSum(root, curr_number):
        nonlocal result
        if root:
            curr_number = curr_number * 10 + root.val
            # if a node is a leaf, then update root-to-leaf sum:
            if root.left == None and root.right == None:
                result += curr_number

            if root.left != None:
                findSum(root.left, curr_number)
            if root.right != None:
                findSum(root.right, curr_number)

    findSum(root, 0)
    return result


"""
Time complexity: O(N) to visit each node
Space: O(H) to keep the recursion stack, where H is a tree height.

"""
