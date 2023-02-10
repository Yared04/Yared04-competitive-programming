import numpy as np
from scipy import signal
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1 = np.flip(np.flip(img1, 0), 1)   
        bigImg = np.zeros((n * 3, n * 3))  
        bigImg[n : 2 * n, n : 2 * n] = img2

        return int(np.max(signal.convolve2d(bigImg, img1)))