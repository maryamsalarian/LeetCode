class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # start from top right. need coordinates [0][j???]
        # number of rows = number of inside arrays = i
        rows = len(matrix)
        # number of cols = number of elements inside a single array = j
        cols = len(matrix[0])
        # starting coordinate
        curr_row = 0
        curr_col = cols - 1
        while curr_row < rows and curr_col >= 0:
            curr = matrix[curr_row][curr_col]
            if curr == target:
                return True
            elif curr < target:
                curr_row += 1
            else:  # target < curr
                curr_col -= 1
        return False
