from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current: Optional[ListNode] = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


def print_result(head: Optional[ListNode]) -> None:
    result: list[int] = []
    current: Optional[ListNode] = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    sol = Solution()
    head: Optional[ListNode] = ListNode(
        1, ListNode(1, ListNode(1, ListNode(1, ListNode(3))))
    )
    result = sol.delete_duplicates(head)
    print(print_result(result))
