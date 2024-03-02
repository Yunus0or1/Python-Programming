

def Solution_Stack():
    def findMaxConnected(graph):
        maximum = 0
        visited = set()

        for node in graph:
            if node in visited:
                continue

            totalNode = 0
            stack = [node]

            while len(stack) > 0:
                current = stack.pop()
                visited.add(current)
                totalNode = totalNode + 1

                for neighbour in graph[current]:
                    if neighbour in visited or neighbour in stack:
                        continue
                    stack.append(neighbour)

            maximum = max(maximum, totalNode)

        return maximum

    def dfs_stack(graph, current):
        visited = set()

        stack = [current]

        while len(stack) > 0:
            current = stack.pop()
            visited.add(current)
            print(current)

            for neighbour in graph[current]:
                if neighbour in visited:
                    continue

                stack.append(neighbour)

class Solution_Recursion():
    maximum = 0
    currentTotal = 0
    visited = set()

    def dfs_recursion_connected_graph(self, graph):
        for node in graph:
            if node not in self.visited:
                self.currentTotal = 0
                self.call_dfs_connected_graph(graph, node)

        return self.maximum

    def call_dfs_connected_graph(self, graph, current):
        self.currentTotal = self.currentTotal + 1
        self.maximum = max(self.maximum, self.currentTotal)
        self.visited.add(current)

        for neighbour in graph[current]:
            if neighbour in self.visited:
                 continue

            self.call_dfs_connected_graph(graph, neighbour)

class Solution_Recursion():
    maximum = 0
    currentTotal = 0
    visited = set()

    def dfs_recursion_connected_graph(self, graph):
        for node in graph:
            if node not in self.visited:
                self.currentTotal = 0
                self.call_dfs_connected_graph(graph, node)

        return self.maximum

    def call_dfs_connected_graph(self, graph, current):
        self.currentTotal = self.currentTotal + 1
        self.maximum = max(self.maximum, self.currentTotal)
        self.visited.add(current)

        for neighbour in graph[current]:
            if neighbour in self.visited:
                continue

            self.call_dfs_connected_graph(graph, neighbour)

class Solution_Recursion_With_NO_GLOBAL_STATE():
    def dfs_recursion_connected_graph(self, graph):
        visited = set()
        maximum = 0
        for node in graph:
            if node not in visited:
                maximum = max(self.call_dfs_connected_graph(graph, node, 0, visited), maximum)

        return maximum

    def call_dfs_connected_graph(self, graph, current, total, visited):
        if current in visited:
            return total

        currentT = total + 1
        visited.add(current)

        for neighbour in graph[current]:
            currentT = self.call_dfs_connected_graph(graph, neighbour, currentT, visited)

        return currentT

graph = {
    0: [1,8,5],
    1: [0],
    8: [0, 5],
    5: [0, 8],

    3: [4, 2],
    4: [3, 2],
    2: [4, 3],
}

print(Solution_Recursion_With_NO_GLOBAL_STATE().dfs_recursion_connected_graph(graph))
