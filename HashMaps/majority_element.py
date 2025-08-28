class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Moore's Voting Algorithm

        counter = 0
        candid = 0
        for num in nums:
            if counter == 0:
                candid = num
                # counter = 1
                # continue
            if num == candid:
                counter += 1
            if num != candid:
                counter -= 1
        return candid

        # hashmap solution:

        target = len(nums) / 2
        hashmap = defaultdict(int)
        for num in nums:  # count all the elements in the array
            hashmap[num] += 1
        for key, count in hashmap:
            if count > target:
                return key
        return 0  # if no majority element found
