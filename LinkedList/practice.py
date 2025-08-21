from typing import Optional


class ListNode(object):
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def remove_duplicates(self, head: ListNode) -> Optional[ListNode]:
        curr: ListNode = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def print_list(self, head: Optional[ListNode]) -> Optional[list[int]]:
        result: list[int] = []
        while head:
            result.append(head.val)
            head = head.next
        return result


if __name__ == "__main__":
    head: Optional[ListNode] = ListNode(
        4,
        ListNode(
            8,
            ListNode(
                8, ListNode(8, ListNode(16, ListNode(16, ListNode(16, ListNode(16)))))
            ),
        ),
    )
    sol: Solution = Solution()
    result: Optional[ListNode] = sol.remove_duplicates(head)
    pending_print: Optional[list[int]] = sol.print_list(result)
    print(pending_print)
