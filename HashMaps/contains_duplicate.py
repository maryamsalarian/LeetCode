class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        # for i in range(len(nums)):
        #     if nums[i] not in visited:
        #         visited.add(nums[i])
        #     else:
        #         return True
        # return False

        # below method is faster
        # for num in nums:
        #     if num not in visited:
        #         visited.add(num)
        #     else:
        #         return True
        # return False

        # one liner:
        return len(set(nums)) < len(
            nums
        )  # if true, at least one element is repeated more than once
