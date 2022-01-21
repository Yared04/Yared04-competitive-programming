class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if n < 4:
                return False
            elif n >= 4: 
                return self.isPowerOfFour(n/3)