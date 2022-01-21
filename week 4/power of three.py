class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            if n < 3:
                return False
            elif n >= 3: 
                return self.isPowerOfThree(n/3)
          