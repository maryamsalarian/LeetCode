# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # # iterative solutoin:
        # my_list = deque([(p, q)])
        # while my_list:
        #     first, second = my_list.popleft()
        #     if not first and not second:
        #         continue
        #     if not first or not second:
        #         return False
        #     if first.val != second.val:
        #         return False
        #     my_list.append((first.left, second.left))
        #     my_list.append((first.right, second.right))
        # return True
        
        # in the recursive technique the p and q are not treated as roots
        # rather they are any two nodes that we compare
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

