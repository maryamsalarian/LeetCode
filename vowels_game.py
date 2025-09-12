class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for char in s:
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                return True
        return False
