class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left_corner = max(rec1[0], rec2[0])
        right_corner = min(rec1[2], rec2[2])
        top_corner = min(rec1[3], rec2[3])
        bottom_corner = max(rec1[1], rec2[1])
        if right_corner-left_corner > 0 and top_corner - bottom_corner > 0:
            return True
            
        return False
