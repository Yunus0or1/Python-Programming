import sys

def findShortest(distance, visited):
    min = sys.maxsize

    for i in range(len(distance)):
        if (distance[i] < min) and (i not in visited):
            min = distance[i]
            min_index = i

    return min_index

def djikstra(graph, src):
    totalNode = len(graph)

    distance = [sys.maxsize] * totalNode
    distance[src] = 0

    visited = set()

    for i in range(totalNode):
        short = findShortest(distance,visited)
        visited.add(short)

        for j in range(len(graph[short])):
            if (graph[short][j] > 0) and (j not in visited) and (distance[j] > distance[short] + graph[short][j]):
                distance[j] = distance[short] + graph[short][j]

    return distance

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]];

print(djikstra(graph,0))
