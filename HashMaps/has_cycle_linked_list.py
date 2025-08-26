from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # hash table implementation:
        
        visited: set = {}  # visited: set = set(). O(1) membership test time. O(n) space
        curr: Optional[ListNode] = head
        # while curr is not None > have not reached the tail
        while curr:
            if curr not in visited:
                # add curr.val to visited and move the head
                visited.add(curr)
                curr = curr.next  # O(n) linked list traversal time
            else:
                # cycle found
                return True
        # reached tail
        return False


# Floy's Tortoise and Hare Algorithm
class Solution2(object):
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast and fast.next:  # O(1) space. O(n) traversal time
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
