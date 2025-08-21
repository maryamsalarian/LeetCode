from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        if not head or not head.next:
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
