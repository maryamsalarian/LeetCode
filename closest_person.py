class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
      # closest person is the one with the shortest distance from z
        x_distance = abs(z - x)
        y_distance = abs(z - y)

        if x_distance > y_distance:
            return 2
        elif x_distance < y_distance:
            return 1
        else:
            return 0
