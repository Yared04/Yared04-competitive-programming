class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        pt1, pt2 = 0, len(people)-1
        ctr = 0
        while pt1 <= pt2:
            if pt1 == pt2:
                ctr += 1
                break
            if people[pt1] + people[pt2] <= limit:
                ctr += 1
                pt1 += 1
                pt2 -= 1
            else:
                ctr += 1
                pt2 -= 1
            
        return ctr