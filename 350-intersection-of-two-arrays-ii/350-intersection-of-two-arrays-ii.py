class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = Counter(nums1)
        res = []
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num]-=1
        return res