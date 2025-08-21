from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        while curr:
            nxt: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # fast and slow pointers

    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        rev_head: Optional[ListNode] = self.rev(slow.next)
        if not head and not rev_head:  # empty linked list is palindrome
            return True
        while head and rev_head:
            if not head.val == rev_head.val:
                return False
            head = head.next  # remember to update the heads
            rev_head = rev_head.next
        return True
