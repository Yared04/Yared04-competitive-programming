class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        items = [(costs[i][1] - costs[i][0], i) for i in range(len(costs))]
        items.sort()
        
        a_count = 0
        res = 0
        for _, idx in items:
            if a_count < len(costs) / 2:
                res += costs[idx][1]
                a_count += 1
            else:
                res += costs[idx][0]
        return res