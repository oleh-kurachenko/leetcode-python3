from typing import List, Optional
from leetcode.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        assert head is not None

        itr = head
        fast_itr = head

        while fast_itr.next and fast_itr.next.next:
            itr = itr.next
            fast_itr = fast_itr.next.next

        rev_itr = itr.next
        itr.next = None

        while rev_itr:
            next_itr = rev_itr.next
            rev_itr.next = itr
            itr = rev_itr
            rev_itr = next_itr

        while head:
            if head.val != itr.val:
                return False
            itr = itr.next
            head = head.next

        return True


if __name__ == '__main__':
    head = ListNode.make_list_node([1, 4, 3, 2, 1])
    print(Solution().isPalindrome(head))
