class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #two pointers, backward merging 1:  
        # better memory performance than below method 2.
        p1 = m-1
        p2 = n-1
        pm = n+m-1
         
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[pm] = nums1[p1]
                p1 -= 1
            else:
                nums1[pm] = nums2[p2]
                p2 -= 1
            pm -= 1
        # if nums2 has leftovers
        while p2 >= 0:
            nums1[pm] = nums2[p2]
            p2 -= 1
            pm -= 1

        return nums1


        # # two pointer 2:

        # p1 = m-1
        # p2 = n-1
        # pm = n+m-1

        # while p2 >= 0:
        #     if p1 >= 0 and nums1[p1] > nums2[p2]:
        #         nums1[pm] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[pm] = nums2[p2]
        #         p2 -= 1
        #     pm -= 1

        # return nums1


        # # python sort function:

        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()

        # return nums1

