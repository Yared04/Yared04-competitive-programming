class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        order = []
        for i in range(len(score)):
            order.append([score[i][k], i])
        order.sort(key = lambda x: x[0], reverse=True)
        sorted_score = []
        for _, idx in order:
            sorted_score.append(score[idx])
        return sorted_score
            
        