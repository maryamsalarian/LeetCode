from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        # dummy node approach:
        dummy: ListNode = ListNode(0, head)
        prev: ListNode = dummy
        curr: Optional[ListNode] = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

        # my initial approach:
        # while head != None and head.val == val:
        #     head = head.next

        # curr = None

        # if head != None:
        #     prev = head
        #     curr = head.next

        # while curr != None:
        #     if curr.val == val:
        #         prev.next = curr.next
        #     else:
        #         prev = curr
        #     curr = curr.next

        # return head
