from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        '''
        -1  : unvisited
        0   : visiting
        1   : visited
        '''
        v = [-1] * numCourses
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)

        def dfs(node):
            nonlocal v
            print(node,v)
            v[node] = 0
            for x in adj[node]:
                if v[x]==0:
                    return False
                v[x] = 0
                if not dfs(x):
                    return False
                v[x] = 1
            v[node] = 1
            return True

        for k,_ in adj.items():
            if not dfs(k):
                return False
        return True

arr = [[1,0],[0,1]]
print(Solution().canFinish(2,arr))
