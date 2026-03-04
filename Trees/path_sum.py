# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # # recusrive solution - poor on memory:
        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return root.val == targetSum
        # remaining = targetSum - root.val
        # return (self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining))

        # # iterative - deque:
        # if not root:
        #     return False
        # my_list = deque([(root, targetSum - root.val)])
        # while my_list:
        #     node, remaining = my_list.popleft()
        #     if not node.left and not node.right and remaining == 0:
        #         return True
        #     if node.let:
        #         my_list.append((node.left, remaining - node.left.val))
        #     if node.right:
        #         my_list.append((node.right, remaining - node.right.val))

        # iterative - stack:
        if not root:
            return False
        my_s = [(root, targetSum - root.val)]
        while my_s:
            node, remaining = my_s.pop()
            if not node.left and not node.right and remaining == 0:
                return True
            if node.left:
                my_s.append((node.left, remaining - node.left.val))
            if node.right:
                my_s.append((node.right, remaining - node.right.val))
        return False

