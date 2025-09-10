from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # intuitive hashmap, 1 hashmap
        
        # s_chars = defaultdict(lambda: 1)
        # for char in s:
        #     if not char in s_chars:
        #         s_chars[char]
        #     else:
        #         s_chars[char] += 1
        # # by the end, s_chars includes all chars and their count for str s
        # for char in t:
        #     if char in s_chars:
        #         s_chars[char] -= 1
        #         if s_chars[char] < 0:
        #             return False
        #         else:
        #             continue
        #     else:
        #         return False
        # # if by then, there are any key:value pair left with value > 0, means that all chars were not matchec > not anagram
        # for char in s_chars:
        #     if s_chars[char] != 0:
        #         return False
        # # return True

        # intuitive hashmap, 2 hashmaps

        if len(s) != len(t):  # ensure lengths are equal
            return False

        s_chars = defaultdict(lambda: 1)
        t_chars = defaultdict(lambda: 1)
        # for str s
        for char in s:
            if not char in s_chars:
                s_chars[char]
            else:
                s_chars[char] += 1
        # for str t
        for char in t:
            if not char in t_chars:
                t_chars[char]
            else:
                t_chars[char] += 1
        for key in s_chars:
            if not key in t_chars:  # ensure key exists in both maps
                return False
            if s_chars[key] != t_chars[key]:
                return False
        return True


        # same method, 2 hashmaps
        # Q: what if we are not allowed lambda and defaultdict?
        # A: alternate implementation using normal sets
        s_chars, t_chars = {}
        # instead of iterating the strings by char, iterate by index since we know they are equal in size
        for i in range(len(s)):
            s_chars[s[i]] = 1 + s_chars.get(s[i], 0)
            t_chars[t[i]] = 1 + t_chars.get(t[i], 0)
        # now both hashmaps are populated, continue with the last for loop to compare them
