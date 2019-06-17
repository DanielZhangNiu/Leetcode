"""
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
    
    Example 1:
    
    Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
    
    0          3
    |          |
    1 --- 2    4
    
    Output: 2
    Example 2:
    
    Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    
    0           4
    |           |
    1 --- 2 --- 3
    
    Output:  1
    Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
class Solution:
    """
    Union Found, AC but slow
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
        
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!=rooty:
            self.parent[rootx] = rooty
            self.cnt -= 1
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return n
        
        self.parent = [i for i in range(n)]
        self.cnt = n
        
        for edge in edges:
            x, y = edge[0], edge[1]
            self.union(x,y)
        return self.cnt
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = [[] for _ in range(n)]
        for node_a, node_b in edges:
            adj_list[node_a].append(node_b)
            adj_list[node_b].append(node_a)
        
        component_count = 0
        visited = set()
        
        def visit(node):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    visit(neighbour)
    
        for node in range(len(adj_list)):
            if node not in visited:
                component_count += 1
                visit(node)

        return component_count
