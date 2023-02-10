class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1, nums2
        if len(nums1) > len(nums2):
            n1, n2 = n2, n1
        total = len(n1) + len(n2)
        half = total // 2
        left,right = 0, len(n1)-1
        while True:
            mid = (left + right)//2
            ptr2 = half - mid - 2
            
            n1Left = n1[mid] if mid >= 0 else -inf
            n2Left = n2[ptr2] if ptr2 >= 0 else -inf
            n1Right = n1[mid+1] if mid + 1 < len(n1) else inf
            n2Right = n2[ptr2+1] if ptr2 + 1 < len(n2) else inf
            
            if n1Left <= n2Right and n2Left <= n1Right:
                if total % 2:
                    return min(n1Right, n2Right)
                return (max(n1Left, n2Left) + min(n2Right, n1Right)) / 2
            elif n2Left > n1Right:
                left = mid + 1
            else:
                right = mid - 1
                
            