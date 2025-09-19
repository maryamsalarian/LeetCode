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

        # one liner:
        return str(x) == str(x)[::-1]

        # reversing the number. mod and floor division:
        # memroy efficient. beats 100%
        num = x # temp holder 
        rev = 0

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x


