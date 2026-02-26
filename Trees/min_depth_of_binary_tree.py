# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # recursive - DFS:
        # note: if one child is null, depth will be 0 by default
        # but we should not consider the null child when calculating depth
        if not root:
            return 0

        # if leaf node
        if not root.right and not root.left:
            return 1

        # if no right child
        if not root.right:
            return 1 + self.minDepth(root.left)

        # if no left child
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
