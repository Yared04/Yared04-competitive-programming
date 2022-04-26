from collections import defaultdict,deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # pass
        indegree = {}
        ingrid = defaultdict(set)
        ans = []
        for i in range(len(recipes)):
            indegree[recipes[i]] = len(ingredients[i]) 
            for j in range(len(ingredients[i])):
                ingrid[ingredients[i][j]].add(recipes[i])
        q = deque(supplies)
        while q:
            cur = q.popleft()
            for recipe in ingrid[cur]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)
                    ans.append(recipe)
        return ans
        
        
        