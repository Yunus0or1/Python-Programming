

def dfs_recursion(graph):
    visited  = set()

    for node in graph:
        if node not in visited:
            call_dfs(graph, node,visited)

def call_dfs(graph, current,visited):
    print(current)
    visited.add(current)

    for neighbour in graph[current]:
        if neighbour in visited:
             continue

        call_dfs(graph, neighbour, visited)


graph = {
    0: [1,8,5],
    1: [0],
    5: [0, 8],
    8: [0, 5],

    2: [4, 3],
    3: [4,2],
    4: [3, 2],
}

dfs_recursion(graph)

