from __future__ import annotations
from typing import Optional, List, Any


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def make_list_node(l: List) -> Optional[ListNode]:
        if len(l) == 0:
            return None

        head = ListNode(l[0])
        itr = head

        for val in l[1:]:
            itr.next = ListNode(val)
            itr = itr.next

        return head
