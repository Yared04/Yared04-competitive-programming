class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dic = defaultdict(int)
        for num in nums2:
            self.dic[num] += 1
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.nums2[index] += val
        self.dic[num] -= 1
        if self.dic[num] == 0:
            self.dic.pop(num)
        self.dic[num + val] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += self.dic[(tot - num)]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)