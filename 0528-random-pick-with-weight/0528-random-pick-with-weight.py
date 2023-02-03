class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.w.append(cur_sum)

    def pickIndex(self) -> int:
        target = random.random() * self.w[-1]
        left, right = 0, len(self.w) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if target > self.w[mid]:
                left = mid
            else:
                right = mid
        if self.w[left] >= target:
            return left
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()