from typing import Optional
from leetcode.ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        while head is not None and head.next is not None:
            head = head.next.next
            slow = slow.next

            if head == slow:
                return True

        return False
