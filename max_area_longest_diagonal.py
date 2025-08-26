# initial solution:


class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        prev_d = 0
        prev_area = 0
        for rectangle in dimensions:
            d = (rectangle[0] ** 2) + (rectangle[1] ** 2)
            area = rectangle[0] * rectangle[1]
            if d > prev_d:
                prev_d = d
                prev_area = area
            elif d == prev_d and area > prev_area:
                prev_area = area
        return prev_area
