import sys
class Solution(object):

    def getShortestNode(self, distance ,visited):
        min = sys.maxsize
        min_index = -1

        for i in range(1, len(distance)):

            if (distance[i] < min) and (i not in visited):
                min = distance[i]
                min_index = i

        return min_index


    def networkDelayTime(self, times, n, k):
        distance = [sys.maxsize] * (n + 1)
        distance[k] = 0

        visited = set()

        for i in range(1, n + 1):
            shortestNode = self.getShortestNode(distance, visited)
            if shortestNode == -1:
                return -1
            visited.add(shortestNode)

            for j in range(len(times)):
                if (times[j][0] == shortestNode) and (distance[times[j][1]] > distance[shortestNode] + times[j][2]):
                    distance[times[j][1]] = distance[shortestNode] + times[j][2]

        distance.pop(0)

        totalUnReachable = 0
        max = -1
        for i in range(len(distance)):
            if distance[i] == sys.maxsize:
                totalUnReachable = totalUnReachable + 1

            if distance[i] > max:
                max = distance[i]

        if totalUnReachable != 0:
            return -1

        return max



# times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# n = 4
# k = 2

# times = [[1,2,1]]
# n = 2
# k = 1

times = [[1,2,1]]
n = 2
k = 2

s = Solution()
print(s.networkDelayTime(times,n,k))