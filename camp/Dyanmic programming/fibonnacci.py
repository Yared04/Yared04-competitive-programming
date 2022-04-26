class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def fibo(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 0
            elif n == 1:
                return 1
            cache[n] = fibo(n-1) + fibo(n-2)             
            return cache[n]
        return fibo(n)