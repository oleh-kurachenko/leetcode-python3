from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = set(nums)
        if 0 in distinct:
            distinct.remove(0)

        return len(distinct)
