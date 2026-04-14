from typing import List


class Solution:
    @staticmethod
    def letterIndex(c: str) -> int:
        return ord(c) - ord('a')

    def __init__(self):
        self.dictionary: List[int] = list(range(0, self.letterIndex('z') + 1))

    def isLexLess(self, s1: str, s2: str) -> bool:
        for i in range(min(len(s1), len(s2))):
            if self.dictionary[self.letterIndex(s1[i])] < self.dictionary[
                self.letterIndex(s2[i])]:
                return True
            if self.dictionary[self.letterIndex(s1[i])] > self.dictionary[
                self.letterIndex(s2[i])]:
                return False
        return len(s1) <= len(s2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, c in enumerate(order):
            self.dictionary[self.letterIndex(c)] = i

        return all(self.isLexLess(words[i], words[i + 1]) for i in
                   range(len(words) - 1))
