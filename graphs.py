from collections import defaultdict
class Graphs:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges=[]

    def add_edges(self, u,v):
        self.graph[u].append(v)

    def generate_edges(self):
        for n in self.graph:
            for neigh in self.graph[n]:
                self.edges.append((n, neigh))
        return self.edges


    def bfs(self, start):
        explored = []
        queue=[start]

        while queue:
            elem = queue.pop(0)
            if elem not in explored:
                explored.append(elem)
                neighbours = self.graph[elem]

                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored



    def path_exist(self, start, end):
        if start == end:
            return 'Found'
        queue=[start]
        visited=[]

        while queue:
            elem = queue.pop(0)
            if elem == end:
                return 'Path exists'
            else:
                if elem not in visited:
                    visited.append(elem)
                    neighbours = self.graph[elem]

                    for n in neighbours:
                        queue.append(n)

        return 'Not Found'



    def dfs(self, start):
        explored=[]
        stack=[start]
        while stack:
            elem = stack.pop()
            if elem not in explored:
                explored.append(elem)
                neighbours = self.graph[elem]

                for n in neighbours:
                    stack.append(n)

        return explored



g= Graphs()
g.add_edges('a','c')
g.add_edges('a','b')
g.add_edges('b','c')
g.add_edges('b','e')
g.add_edges('c','d')
g.add_edges('c','a')
g.add_edges('c','b')
g.add_edges('c','a')
g.add_edges('e','b')
g.add_edges('d','c')
g.add_edges('e','c')

print(g.path_exist('a', 'd'))