# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Input: root = [3,9,20,null,null,15,7]
        # Output: 3
        # root is not simply an array, it is a TreeNode object

        # iterative solution - BFS:
        # analyze one level first
        # increase depth second
        # move to the next level

        if not root:
            return 0
            # root is null
            # depth is 0

        my_list = deque([root])
        depth = 0

        while my_list:
            for i in range(len(my_list)):
                node = my_list.popleft()
                if node.right:
                    my_list.append(node.right)
                if node.left:
                    my_list.append(node.left)
            # for loop ends when all items in initial list are popped
            # this means the level is completely processed
            depth += 1
        # while loop ends when my_list is empty
        # all levels have been processed, no unprocessed nodes left
        return depth


        # recursive solution - DFS:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


        # recursion in C:
        # include <stdlib.h>
        # static int max(int a, int b) {
        #     return (a > b) ? a : b;
        # }
        # int maxDepth(struct TreeNode* root) {
        #     if (root == NULL) return 0;
        #     return 1 + max(maxDepth(root->left), maxDepth(root->right));
        # }

