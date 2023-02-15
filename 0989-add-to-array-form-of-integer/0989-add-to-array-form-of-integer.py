class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        _num = 0
        x = len(num) - 1
        for i in range(x+1):
            _num += num[i] * 10**x
            x -= 1
        _num += k
        return list(map(int, list(str(_num))))
        