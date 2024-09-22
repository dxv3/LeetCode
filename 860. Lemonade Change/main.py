class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ** 0.5 % 1 == 0:
            if ((n ** 0.5) ** 2) == n:
                return True
            else:
                return False
    
print(Solution().isPowerOfTwo(8))