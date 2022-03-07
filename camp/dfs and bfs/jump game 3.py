class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque([start])
        visited = set()
        valid = lambda idx : 0 <= idx < len(arr)
        while q:
            current = q.popleft()
            if arr[current] == 0:
                return True
            visited.add(current)            
            left = current + arr[current]
            right = current - arr[current]
            if valid(left) and left not in visited:
                q.append(left)
                if arr[left] == 0: return True 
                # visited.add(left)
            if valid(right) and right not in visited:
                q.append(right) 
                if arr[right] == 0: return True 
                # visited.add(right)
        return False
                