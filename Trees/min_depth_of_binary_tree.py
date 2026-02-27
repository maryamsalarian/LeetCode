# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # iterative - BFS:
        # from collections import deque
        if not root:
            return 0
        my_list = deque([root])
        depth = 1
        while my_list:
            for i in range(len(my_list)):
                node = my_list.popleft()
                if node.right:
                    my_list.append(node.right)
                if node.left:
                    my_list.append(node.left)
                if not node.left and not node.right:
                    return depth
            # return if encountered a leaf node, otherwise finish the level
            depth += 1
        return depth

        # recursive - DFS:
        # note: if one child is null, depth will be 0 by default
        # but we should not consider the null child when calculating depth
        # if not root:
        #     return 0

        # # if leaf node
        # if not root.right and not root.left:
        #     return 1

        # # if no right child
        # if not root.right:
        #     return 1 + self.minDepth(root.left)

        # # if no left child
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        
        # return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
