from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head):
        """
        #     :type head: Optional[ListNode]
        #     :rtype: bool
        #"""
        stack: list[Optional[ListNode]] = []
        curr: ListNode = head
        while head:
            stack.append(head.val)
            head = head.next
        while stack and curr:
            if stack.pop() == curr.val:
                curr = curr.next
                continue
            else:
                return False
        return True
