# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA: ListNode = headA
        pB: ListNode = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
