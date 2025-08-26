class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """

        # initial solution:

        # prev_d = 0
        # prev_area = 0
        # for rectangle in dimensions:
        #     d = (rectangle[0] ** 2) + (rectangle[1] ** 2)
        #     area = rectangle[0] * rectangle[1]
        #     if d > prev_d:
        #         prev_d = d
        #         prev_area = area
        #     elif d == prev_d and area > prev_area:
        #         prev_area = area
        # return prev_area

        # improved solution:

        max_d = 0
        max_area = 0
        for h, w in dimensions:
            area = h * w
            d = h * h + w * w
            if d > max_d:
                max_d = d
                max_area = area
            if d == max_d:
                max_area = max(max_area, area)
        return max_area
