class Solution:
    def __init__(self) :
        self.numbers = []

    def fizzBuzz(self, n):
        if n>10000:
            return None
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                x = "FizzBuzz"
            elif x % 3 == 0:
                x = "Fizz"
            elif x % 5 == 0:
                x = "Buzz"
            self.numbers.append(str(x))
        print(self.numbers)
        return self.numbers
