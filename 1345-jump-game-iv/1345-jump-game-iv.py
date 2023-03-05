class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         print(len(arr))
#         dict = {}
        
#         for idx in range(len(arr)):
#             if arr[idx] in dict:
#                 dict[arr[idx]].append(idx)
#             else:
#                 dict[arr[idx]] = [idx]
#         bound = lambda row: row >= 0 and row < len(arr)
#         parents = collections.deque([])
#         children = collections.deque([])
#         visited = set()
#         parents.append([0,0])
#         visited.add(0)
        
#         while parents or children:
#             while parents:
#                 parent = parents.popleft()
#                 # print(parent)
#                 level = parent[1]
#                 if parent[0] == len(arr) - 1:
#                     return level
#                 nxt = parent[0] + 1
#                 prev = parent[0] - 1
#                 lis = dict[arr[parent[0]]]
#                 # listi = []
#                 # listi.append(nxt)
#                 # listi.append(prev)
#                 # listi.append(lis)
#                 if bound(nxt) and nxt not in visited:
#                     children.append([nxt, level + 1])
#                     visited.add(nxt)
#                 if bound(prev) and prev not in visited:
#                     children.append([prev, level + 1])
#                     visited.add(prev)
#                 while lis:
#                     idx = lis.pop()
#                     children.append([idx, level + 1])
#                     visited.add(idx)
#                 # for elem in listi:
#                 #     if type(elem) == type([]):
#                 #         while elem:
#                 #             idx = elem.pop()
#                 #             children.append([idx, level + 1])
#                 #             visited.add(idx)
#                 #     elif not bound(elem) or elem in visited:
#                 #                     continue
#                 #     else:
#                 #         children.append([elem, level + 1])
#                 #         visited.add(elem)
#             while children:
#                 child = children.popleft()
#                 parents.append(child)