class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for start, dest, weight in edges:
            graph[start].append((dest, weight))
            graph[dest].append((start, weight))
        
        def djikstra(cities, visited, distance_to_city):
            while cities:
                distance, cur_city = heappop(cities)
                if cur_city in visited:
                        continue
                visited.add(cur_city)
                for dest, weight in graph[cur_city]:
                    if distance_to_city[dest] >= weight + distance:
                        distance_to_city[dest] = weight + distance
                        heappush(cities, (distance_to_city[dest], dest))
                    
            cities_under_threshold = 0
            for s in distance_to_city:
                if s and s <= distanceThreshold:
                    cities_under_threshold += 1
            return cities_under_threshold
        
        reachable_cities_from = {}
        
        for i in range(n):
            dist_to_city =  [float('inf')] * (n)
            dist_to_city[i] = 0
            reachable_cities_from[i] = djikstra([(0, i)], set(), dist_to_city)
        
        res = (0, float('inf'))
        for key, val in reachable_cities_from.items():
            if val < res[1]:
                res = (key, val)
            elif val == res[1]:
                res = (max(key, res[0]), val)
        return res[0]
                
            
            
                    
                
            