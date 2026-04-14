from typing import Optional
from leetcode.ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val is None:
                return True
            head.val = None
            head = head.next

        return False
