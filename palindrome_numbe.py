class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

      # somehow i found the worst runtime of all! 
        array_x = []
        
        for num in str(x):
            array_x.append(num)
        reverse_array_x = array_x[::-1]

        for i in range(len(array_x)):
            if array_x[i] != reverse_array_x[i]:
                return False
        return True
