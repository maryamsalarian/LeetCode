from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        while curr:
            next_node: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # two pointer switching approach:
        pA: ListNode = headA
        pB: ListNode = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

        # my original approach: reverse lists and match them from the end
        # problem: alters the structure of the linked lists. unreliable in finding edge cases
        # new_headA: Optional[ListNode] = self.reverse_list(headA)
        # new_headB: Optional[ListNode] = self.reverse_list(headB)
        # last_matching_node: Optional[ListNode] = None
        # pA: Optional[ListNode] = new_headA
        # pB: Optional[ListNode] = new_headB
        # while pA and pB:
        #     if pA is pB:
        #         last_matching_node = pA
        #         break
        #     pA = pA.next
        #     pB = pB.next
        # self.reverse_list(new_headA)
        # self.reverse_list(new_headB)
        # return last_matching_node
