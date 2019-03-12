#Uses python3

import sys

# Complete maze problem coursera.

def reach(adj, x, y):
    #write your code here
    visited = [False]*len(adj)
    #print('visited', visited)
    def dfs(x):
        visited[x] = True
        for i in adj[x]:
            if i == y:
                visited[i] = True
                return 1

            else:
                if visited[i] == False:
                    dfs(i)
        return 0
    return dfs(x)


    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #print ('data', data)
    n, m = data[0:2]
    # n  is no. of vertices
    # m is no. of edges from 1st row second column of input
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #print('edges', edges)
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    #print('adj blank list', adj)
    x, y = x - 1, y - 1
    for (a, b) in edges:
        #print('a', a)
        #print('b', b)
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print('adjacency final list', adj)
    print(reach(adj, x, y))