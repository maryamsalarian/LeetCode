class Solution(object):
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
      # find element in the larger array
      # continue traversing the large array until next greatest is found
      # if not, use -1 as value
      # append value to a predefined result list/array and return
        result: list[int] = []
        found = None
        for i in nums1:
            # find element in nums2
            for j_index, j in enumerate(nums2):
                if i == j:
                    found = j
                    break
            # find next index with a bigger value
            for k_index in range(j_index, len(nums2)):
                if nums2[k_index] > found:
                    result.append(nums2[k_index])
                    break
            else:
                result.append(-1)
        return result
