def dfs(u , prev , adj,result):
    result.append(u)
    for v in adj[u]:
        if v != prev:
            dfs(v,u,adj,result)
def restoreArray(adjacentpairs):
    result = []
    adj = {}
    for u , v in adjacentpairs:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    startpoint = None
    for vec in adj:
        if len(adj[vec]) == 1:
            startpoint = vec
    dfs(startpoint,None,adj,result)
    return result 
adjacentPairs = [[2,1],[3,4],[3,2]]
print(restoreArray(adjacentPairs))
adjacentPairs = [[4,-2],[1,4],[-3,1]]
print(restoreArray(adjacentPairs))
