# Last updated: 28.4.2025, 12:59:28
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

        if not root:
            return False
            
        if not root.left and not root.right:
            return targetSum == root.val

        if root.left and root.right:
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        elif root.left:
            return self.hasPathSum(root.left, targetSum-root.val)
        else:
            return self.hasPathSum(root.right, targetSum-root.val)

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

        