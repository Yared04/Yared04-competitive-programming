class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 0: return 1
            if n == 1: return x
            if n % 2 == 0:
                temp = power(x, n//2)
                return temp*temp
            else:
                temp = power(x, n//2)
                return temp*temp*x
        return power(x,n) if n >= 0 else 1/power(x,-n)