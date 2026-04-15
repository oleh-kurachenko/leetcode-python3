from typing import List


class Solution:
    @staticmethod
    def letterIndex(c: str) -> int:
        return ord(c) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:
        count: List[int] = [0] * (self.letterIndex('z') + 1)

        for i in range(len(s)):
            count[self.letterIndex(s[i])] += 1
        for i in range(len(t)):
            count[self.letterIndex(t[i])] -= 1

        return all(c == 0 for c in count)
