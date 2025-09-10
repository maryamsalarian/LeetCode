class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        h_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 2000}
        for i in range(len(s)):
            if i + 1 < len(s) and h_map[s[i]] < h_map[s[i + 1]]:
                result -= h_map[s[i]]
            else:
                result += h_map[s[i]]
        return result

    """
    notes:
    1. how to initiate a hashmap
    2. how to access elements in a hashmap
    ------------------------------------------
    3. how to iterate/read the str s one by one a.k.a access chars
    ------------------------------------------
    4. for loop exit condition
    5. how to handle comparing one char with its following char - edge: there may be no "next" char
    6*. which condition makes the if-else shorter when it comes first - handle the odd one in the if clause, leave the rest to "else" 

    """
