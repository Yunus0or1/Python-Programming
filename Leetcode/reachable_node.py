from typing import List


class Solution:
    def convertToAdjanecyList (self,edges: List[List[int]] ) -> dict:
        graph = {}

        for edge in edges:

            key1 = edge[0]
            key2 = edge[1]

            if key1 not in graph:
                graph[key1] = [key2]
            else:
                currentList = graph[key1]
                currentList.append(key2)
                graph[key1] = currentList

            if key2 not in graph:
                graph[key2] = [key1]
            else:
                currentList = graph[key2]
                currentList.append(key1)
                graph[key2] = currentList

        return graph
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = self.convertToAdjanecyList(edges)
        visited = set()
        stack = [0]
        totalTraverse = 0

        for x in restricted:
            visited.add(x)

        while len(stack) > 0:
            value = stack.pop()

            if value in visited:
                continue

            visited.add(value)
            totalTraverse += 1

            for neighbour in graph[value]:
                stack.append(neighbour)

        return totalTraverse



n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]
print(Solution().reachableNodes(n, edges, restricted))