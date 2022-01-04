class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        elif n > 0: 
            if n % 2 != 0: 
                return  self.myPow(x * x , n//2) * self.myPow(x , 1)
            return self.myPow(x * x , n/2)
        elif n < 0:
            if n % 2 != 0:
                return self.myPow(1/(x * x), (-n) // 2) * self.myPow(1 / x, 1)
            return self.myPow(1/(x * x), (-n) // 2)
        