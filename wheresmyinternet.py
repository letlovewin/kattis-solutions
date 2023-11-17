from collections import deque

class Undirected_Graph:
    #For this undirected graph class you MUST convert all vertices to a dictionary before initializing the object! CRITICAL!
    def __init__(self,nodes,vertices):
        self.vertices = vertices
        self.nodes = nodes
    def deg(self):
        return(len(self.vertices))
        
    def bft(self,origin):
        if not origin in self.vertices:
            return
        q = deque()
        q.append(origin)
        visited = set()
        visited.add(origin)
        while len(q)>0:
            k = q.pop()
            for i in self.vertices[k]:
                if not i in visited:
                    q.append(i)
                visited.add(i)
        return visited
        
    def bfs(self,origin,goal):
        if not origin in self.vertices:
            return
        if origin==goal:
            return set([origin])
        q = deque()
        q.append(origin)
        visited = set()
        visited.add(origin)
        while len(q)>0:
            k = q.pop()
            for i in self.vertices[k]:
                if not i in visited:
                    q.append(i)
                visited.add(i)
                if i==goal:
                    return visited
        return -1
def solve():
    n,m = map(int,input().split(' '))
    d = { i+1:[] for i in range(n) }
    for _ in range(m):
        h1,h2 = map(int,input().split(' '))
        d[h1].append(h2)
        d[h2].append(h1)
    g = Undirected_Graph([i+1 for i in range(n) ],d)
    u = set(g.bft(1))
    if len(u)==n:
        print("Connected")
        return
    j = []
    for i in range(n):
        if not i+1 in u:
            j.append(i+1)
    j.sort()
    for i in j:
        print(i)
    
solve()