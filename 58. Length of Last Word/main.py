class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last = words[-1]
        return len(last)