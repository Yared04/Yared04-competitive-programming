class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        length = len(scores)
        heap = []
        for i in range(length):
            heappush(heap, (ages[i], scores[i]))
        
        new_scores = []
        new_ages = []
        while heap:
            age, score = heappop(heap)
            new_scores.append(score)
            new_ages.append(age)
        dp = [0 for _ in range(length)]
        max_score = 0
        for i in range(length):
            _max = 0
            for j in range(i):
                if new_scores[i] >= new_scores[j]:
                    _max = max(_max, dp[j])
            dp[i] = new_scores[i] + _max
            
            max_score = max(max_score, dp[i])
        return max_score