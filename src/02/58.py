class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        num %= 9
        return num if num else 9