class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       # cache = {}
        # def stepCount(idx):
        #     if idx in cache:
        #         return cache[idx]
        #     if idx > len(cost) - 1:
        #         return 0
        #     by_1 = stepCount(idx+1)
        #     by_2 = stepCount(idx+2)
        #     cache[idx] = cost[idx] + min(by_1, by_2)
        #     return cache[idx]
        # return min(stepCount(0),stepCount(1))
        #        
        step1 = cost[0]
        step2 = cost[1]
        currentStep = 0
        for i in range(2,len(cost)):
            currentStep = cost[i] + min(step1, step2)
            step1 = step2
            step2 = currentStep
        return min(step1,step2)
    
        step1 = 0
        step2 = 0
        currentStep = 0
        for i in range(len(cost)-1,-1,-1):
            currentStep = cost[i] + min(step1, step2)
            step2 = step1
            step1 = currentStep
        return min(step1,step2)
        
        
       