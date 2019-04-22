"""
    Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
    
    
    
    Example:
    
    
    
    Input:
    {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
    
    Explanation:
    Node 1's value is 1, and it has two neighbors: Node 2 and 4.
    Node 2's value is 2, and it has two neighbors: Node 1 and 3.
    Node 3's value is 3, and it has two neighbors: Node 2 and 4.
    Node 4's value is 4, and it has two neighbors: Node 1 and 3.
    
    
    Note:
    
    The number of nodes will be between 1 and 100.
    The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
    Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
    You must return the copy of the given node as a reference to the cloned graph.

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val,[])
        visited = {node:nodeCopy}
        #visited[node] = nodeCopy #在visited数组中，key值为原来的node，value为新clone的node，
        queue = collections.deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                # visit 永远是{1:1},{2:2} 只是作为遍历来用
                #如果一个node不存在于map中，说明这个node还未被clone，将它clone后放入queue中继续处理neighbors
                if neighbor not in visited:
                    # node copynode
                    neighborcopy = Node(neighbor.val,[])
                    # visited{1:1}, visited{2:2},加入visit中
                    visited[neighbor] = neighborcopy
                    # 之前的visit中复制的node都加入边的关系，即每次都把原来node的neighor到自己身上
                    #visited[current].neighbors.append(visited[neighbor])
                    # 处理neighbor, 加入queue中
                    queue.append(neighbor)
                
                # 变成无向图，互相neighbor一下
                visited[current].neighbors.append(visited[neighbor])
        return nodeCopy

