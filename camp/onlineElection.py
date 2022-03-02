class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winner = {}
        self.count = {}
        self.max = 0
        for i in range(len(self.persons)):
            if self.persons[i] not in self.count:
                self.count[self.persons[i]] = 1
                if self.count[self.persons[i]] >= self.max:
                    self.max = self.count[self.persons[i]]
                    self.winner[i] = self.persons[i]
                else:
                    self.winner[i] = self.winner[i-1]
                
            else:
                self.count[self.persons[i]] += 1
                if self.count[self.persons[i]] >= self.max:
                    self.max = self.count[self.persons[i]]
                    self.winner[i] = self.persons[i]
                else:
                    self.winner[i] = self.winner[i-1]
            # print(self.count, self.max, self.winner)
            
        
       
            

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        while left <= right:
            mid = (left + right)//2
            if self.times[mid] > t:
                right = mid -1
                if right < mid:
                    mid = right
                
            elif self.times[mid] < t:
                left = mid + 1
                
            else:
                break
        
        return self.winner[mid]
        
    
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)