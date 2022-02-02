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

    """
    - use a is_order_left to get the zigzag order of BFS
    """

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        """
        from collections import deque

        result = []
        level_list = deque()
        if root is None:
            return []

        # start with the level 0 with a delimeter
        node_queue = deque([root, None])
        # is_order_left: go from left to right for true
        # from right to left if false
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            # at a current level
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            # at a new level
            else:
                # we finish one level
                result.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return result
