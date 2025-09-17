class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # method 1: using nested for loop. time: O(n^2). memroy: O(n)
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    result.append(num1)
        no_dupes = set(result)
        return list(no_dupes)
        return set(result)

