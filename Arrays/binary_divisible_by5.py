class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        # answer = [None] * len(nums)
        # for i in range(len(nums)): # O(n^2). very inefficient.
        #     total = 0
        #     for j in range(0,i+1): # keep i in the range by writing: i+1
        #         if nums[j] == 1:
        #             total += (2 ** (i-j))
        #     answer[i] = (total % 5 == 0)

        # return answer

        
        # given [0,1,1]:
        # 0             > 0
        # add 1 (0,1)   > 1
        # add 1 (0,1,1) > 3
        # new_val = prev_val * 2 + new_bit

        answer = []
        val_mod = 0
        for i in range(len(nums)): # O(n) time
            val_mod = (val_mod * 2 + nums[i]) % 5
            answer.append(val_mod == 0)
        return answer
