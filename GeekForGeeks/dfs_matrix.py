def dfs(graph):
    row = len(graph)
    col = len(graph[0])
    visited = set()
    result = []

    def isValidPosition(i, j):
        if i < 0 or i > row - 1:
            return False
        if j < 0 or j > col - 1:
            return False
        return True

    dR = [ -1, 0,1, 0, ]
    dC = [ 0,-1, 0, 1, ]

    stack = [[0, 0]]

    while len(stack) != 0:
        [x, y] = stack.pop()

        key = str(x) + "_" + str(y)
        if key not in visited:
            result.append(graph[x][y])
            visited.add(key)

        for i in range(0, 4):
            nX = x + dR[i]
            nY = y + dC[i]

            if not isValidPosition(nX, nY):
                continue

            nKey = str(nX) + '_' + str(nY)
            if nKey in visited:
                continue

            stack.append([nX, nY])

    return result


graph = [[3, 3,6,5],
         [1, 1,2,6],
         [9, 8,2,4]]
print(dfs(graph))