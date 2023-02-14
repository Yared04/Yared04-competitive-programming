class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [-i for i in range(1,n)]
        res.append(n*(n-1)/2)
        return res
        