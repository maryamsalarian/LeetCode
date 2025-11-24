class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        answer = [None] * len(nums)
        for i in range(len(nums)): # O(n^2). very inefficient.
            total = 0
            for j in range(0,i+1): # keep i in the range by writing: i+1
                if nums[j] == 1:
                    total += (2 ** (i-j))
            answer[i] = (total % 5 == 0)

        return answer
        