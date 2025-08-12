from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None

        while curr != None:
            nxt: ListNode = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # return prev

        # if return type was list:
        # new_head: Optional[ListNode] = prev
        # result: list[ListNode] = []
        # while new_head != None:
        #     result.append(new_head.val)
        #     new_head = new_head.next
        # return result
