# Given the root of a binary tree, return its maximum depth.


def maxDepth(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth, right_depth)