class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        a = list(map(int, list(a)))
        b = list(map(int, list(b)))
        carry = 0   
        while a or b or carry:
            if a:
                carry += a.pop()
            if b:
                carry += b.pop()

            res.append(str(carry % 2))
            carry //= 2

        return "".join(res[::-1])