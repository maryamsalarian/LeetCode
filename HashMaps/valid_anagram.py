from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # intuitive hashmap, 1 hashmap
        s_chars = defaultdict(lambda: 1)
        for char in s:
            if not char in s_chars:
                s_chars[char]
            else:
                s_chars[char] += 1
        # by the end, s_chars includes all chars and their count for str s
        for char in t:
            if char in s_chars:
                s_chars[char] -= 1
                if s_chars[char] < 0:
                    return False
                else:
                    continue
            else:
                return False
        # if by then, there are any key:value pair left with value > 0, means that all chars were not matchec > not anagram
        for char in s_chars:
            if s_chars[char] != 0:
                return False
        # return True
