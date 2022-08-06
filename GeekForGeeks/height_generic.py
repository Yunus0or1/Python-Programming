
def height_generic(graph):
    n = len(graph)
    dict = {}

    for i in range (0,n):
        dict[i] = []

    for i in range(1,n):
        dict[parent[i]] = dict[parent[i]] + [i]


    queue = [0]
    root={0: 0}
    level = 0
    while(len(queue) != 0):
        value = queue.pop(0)

        for node in dict[value]:
            root[node] = root[value] + 1
            queue.append(node)

            if(root[node] > level):
                level = root[node]

    return level


parent = [-1, 0, 1, 2, 3]
print(height_generic(parent))