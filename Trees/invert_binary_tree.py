# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        my_list = deque([root])
        while my_list:
            node = my_list.popleft()
            # temp = node.left
            # node.left = node.right
            # node.right = temp
            # or - tuple unpacking:
            node.left, node.right = node.right, node.left
            if node.left:
                my_list.append(node.left)
            if node.right:
                my_list.append(node.right)
        return root

        # or recursive:
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        