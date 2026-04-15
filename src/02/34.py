from typing import List, Optional
from leetcode.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        assert head is not None

        itr = head
        length = 0
        while itr:
            length += 1
            itr = itr.next

        l : List[int] = [0] * length
        i = 0
        while i < length:
            l[i] = head.val
            head = head.next
            i += 1

        return all(l[i] == l[len(l) - i - 1] for i in range(int(len(l) / 2)))


if __name__ == '__main__':
    head = ListNode.make_list_node([1, 4, 3, 2, 1])
    print(Solution().isPalindrome(head))
