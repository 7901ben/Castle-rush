graph={
    'A':['B','C','D'],
    'B':['E'],
    'C':['D'],
    'D':[],
    'E':[]
}

visited=set()
    
def dfs(graph, visited , start):
    if start not in visited:
        print(start)
        visited.add(start)
        
    for next in graph[start]:
        dfs(graph,visited,next)

print(dfs(graph,visited,'A'))

