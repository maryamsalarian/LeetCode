class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        h_map = {}
        for index, val in enumerate(nums):
            diff: int = target - val
            if diff in h_map:
                return [h_map[diff], index]
            h_map[val] = index
        return


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([5, -1, 8, 10, 2], 9))
    print(s.twoSum([10, 5, -12, 7], -5))
    print(s.twoSum([2, 5, 11, 15], 9))
    print(s.twoSum([3], 6))
    print(s.twoSum([], 9))
    print(s.twoSum([3, 2, 4, 9, 3], 6))
    print(s.twoSum([3, 2, 0, 4, 3, 0], 0))
