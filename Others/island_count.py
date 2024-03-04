
class Solution_Stack():
    def findMinIsland(self, islands):
        minimum = 999
        visited = set()

        rowLen = len(islands)
        colLen = len(islands[0])

        for i in range (rowLen):
            for j in range (colLen):

                position = str(i) + ',' + str(j)

                if position in visited:
                    continue

                current = islands[i][j]

                if current == 'W':
                    continue

                stack = [[i,j]]
                totalIsland = 0

                while len(stack) > 0:
                    stackCurrent = stack.pop()
                    [rowIndex, colIndex] = stackCurrent

                    rowInBound = 0 <= rowIndex < rowLen
                    colInBound = 0 <= colIndex < colLen

                    if not rowInBound or not colInBound:
                        continue

                    if islands[rowIndex][colIndex] == 'W':
                        continue

                    stackPosition = str(rowIndex) + ',' + str(colIndex)

                    if stackPosition in visited:
                        continue

                    visited.add(stackPosition)
                    totalIsland += 1

                    stack.append([rowIndex + 1, colIndex])
                    stack.append([rowIndex - 1, colIndex])
                    stack.append([rowIndex , colIndex + 1])
                    stack.append([rowIndex , colIndex - 1])

                minimum = min(minimum, totalIsland)

        return minimum
class Solution_Recursion():
    def findMinIsland(self, islands):
        minimum = 999
        visited = set()

        rowLen = len(islands)
        colLen = len(islands[0])

        for i in range (rowLen):
            for j in range (colLen):
                position = str(i) + ',' + str(j)

                if position in visited:
                    continue

                if islands[i][j] == 'W':
                    continue

                totalIsland = self.explore(islands, visited , i, j)
                minimum = min(totalIsland, minimum)

        return minimum
    def explore(self, islands, visited, rowIndex, colIndex):
        rowBound = 0 <= rowIndex < len(islands)
        colBound =  0 <= colIndex < len(islands[0])
        position = str(rowIndex) + ',' + str(colIndex)

        if not rowBound or not colBound:
            return 0

        if position in visited:
            return 0

        if islands[rowIndex][colIndex] == 'W':
            return 0

        visited.add(position)
        total = 1

        total += self.explore(islands, visited, rowIndex + 1, colIndex)
        total += self.explore(islands, visited, rowIndex - 1, colIndex)
        total += self.explore(islands, visited, rowIndex , colIndex+ 1 )
        total += self.explore(islands, visited, rowIndex , colIndex  - 1)


        return total

islands = [
    ['W', 'L', 'W', 'W', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'L', 'W'],
    ['W', 'L', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'L', 'L', 'W'],
    ['W', 'W', 'W', 'L', 'L', 'W'],
    ['W', 'W', 'W', 'L', 'W', 'W'],
]
print(Solution_Recursion().findMinIsland(islands))

islands2 = [
    ['L', 'L', 'L'],
]
print(Solution_Recursion().findMinIsland(islands2))

