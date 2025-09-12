class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 100% runtime:

        # set_nums = set(nums)
        # for i in range(0, len(nums)+1):
        #     if i not in set_nums:
        #         return i


        # using the sum of n consecutive numbers
        # 90% memory:
        
        nums.sort()
        n = len(nums)
        expected_sum = (n) * (n+1) //2 # floor division
        actual_sum = sum(nums)
        return expected_sum - actual_sum
