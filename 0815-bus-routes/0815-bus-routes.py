class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if(source==target):
            return 0
        graph = defaultdict(list)
        for route in range(len(routes)):
            for loc in routes[route]:
                graph[loc].append(route)
        q = [source]
        visited = set()
        ans = 0
        while(q):
            for i in range(len(q)):
                cur = q.pop(0)    
                for route in graph[cur]:
                    if(route in visited):
                        continue
                    visited.add(route)
                    for stop in routes[route]:
                        if(stop == target):
                            return ans+1
                        else:
                            q.append(stop)
            ans+=1
        return -1