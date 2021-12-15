import math
def kClosest(points, k):
   distance=dict()
   output=[]
   for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        length = math.sqrt(x**2 +y**2)
        distance[length] = points[i]
        l = list(distance.items())
        l.sort()
        point = dict(l)
   for key,val in point.items():
       output.append(point[key])
       
   return output[:k]
points = [[1,3],[-2,2]]
print(kClosest(points,1))
# arr =[]
# for idx, val in enumerate(points):
#     print(idx)
#     x= val[0]
#     y= val[1]
#     length = math.sqrt(x**2 +y**2)
#     arr.append(str(idx)+str(length))
# print(arr)
    