# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    # def mirror(self, a, b):
    #     if not a and not b:
    #         return True
    #     if not a or not b:
    #         return False
    #     if a.val != b.val:
    #         return False
    #     return self.mirror(a.left, b.right) and self.mirror(a.right, b.left)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # if no root -> true
        # if no left and no right -> single node -> true
        # compare the nodes that are SUPPOSED to be similar

        # recursive solution -  mirror funciton:
        # return True if not root else self.mirror(root.left, root.right)

        # iterative solution - deque:
        # add the pairs to be compared as a tuple to the deque
        if not root:
            return True
        
        my_list = deque([(root.left, root.right)])
        while my_list:
            a, b = my_list.popleft()
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            my_list.append((a.left, b.right))
            my_list.append((a.right, b.left))
        return True

            