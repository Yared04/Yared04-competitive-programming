class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) == r * c:
            nums = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    nums.append(mat[i][j])
            newMat = []
            idx = 0
            for i in range(r):
                temp = []
                for j in range(c):
                    temp.append(nums[idx])
                    idx +=1
                newMat.append(temp)
            return newMat
        else: return mat
        
        