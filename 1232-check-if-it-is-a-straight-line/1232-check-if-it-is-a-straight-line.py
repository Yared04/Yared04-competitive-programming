class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return True
        _x = coordinates[1][0] - coordinates[0][0]
        _y = coordinates[1][1] - coordinates[0][1]
        for x,y in coordinates:
            if (y - coordinates[0][1]) * _x != _y * (x - coordinates[0][0]):
                return False
        return True