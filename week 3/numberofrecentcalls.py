class RecentCounter:
    
    def __init__(self):
        self.request = deque()
        
    def ping(self, t: int) -> int:
        self.request.append(t)
      
        for i in range(len(self.request)):
            if self.request[0] < t-3000:
                   self.request.popleft()
              
        return len(self.request)
      
