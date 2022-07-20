
def dfs(graph):
    stack = [1]
    result = []

    visited = set()

    while(len(stack)!=0):
        value = stack.pop()

        if value not in visited:
            result.append(value)
            visited.add(value)

        for node in graph[value]:
            if node not in visited:
                stack.append(node)

    return result


graph = {
    1: [6,2],
    2:[1,3],
    3:[2,6,4],
    4:[3,5],
    5: [4,6],
    6: [3,1,5]
}
#
# graph = {
#     1: [6,2],
#     2:[5,3],
#     3:[9,4,5],
#     4: [],
#     5: [],
#     6:  [],
#     9: []
#
# }

print(dfs(graph))