class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        output = [0] * k
        id_min_map = defaultdict(set)
        for _id, time in logs:
            id_min_map[_id].add(time)
        
        for key, val in id_min_map.items():
            output[len(val) - 1] += 1
            
        return output