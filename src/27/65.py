from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        e1 = nums[0]
        e2 = None
        count = -1
        max_count = -1
        for i in range(1, len(nums)):
            if not e2:
                if nums[i] - nums[i - 1] == 1:
                    e2 = nums[i]
                    count = 2
                else:
                    e1 = nums[i]
                continue

            if nums[i] == e1:
                count += 1
                e1 = e2
                e2 = nums[i]
            else:
                e1 = nums[i - 1]
                e2 = nums[i] if nums[i] - nums[i - 1] == 1 else None
                max_count = max(max_count, count)
                count = 2 if e2 else -1

        return max(max_count, count)

if __name__ == '__main__':
    print(Solution().alternatingSubarray([2, 3, 4, 3, 4]))
