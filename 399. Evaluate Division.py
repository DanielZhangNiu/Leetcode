"""
    Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
    
    Example:
    Given a / b = 2.0, b / c = 3.0.
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
    return [6.0, 0.5, -1.0, 1.0, -1.0 ].
    
    The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
    
    According to the example above:
    
    equations = [ ["a", "b"], ["b", "c"] ],
    values = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
    The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    if not equations: return 0
    if len(equations) != len(values): return 0

    # Build the graph first
    graph = {}
    buidlpath(equations,values)
    return[findpath[query] for query in queries]


def buildpath(equations,values):
    def addedge(x,y,value):
        if x in graph:
            graph[x].append((y,value))
        else:
            graph[x] = [(y,value)]
    
    for i in range(len(equations)):
        a, b = equations[i][0],equations[i][1]
        value = values[i]
        addedge(a,b,value)
        addedge(b,a,1.0/value)
        #directed graph, with different weight

def findpath(query):
    x, y = query[0],query[1]
    visited = set()
    if x == y: return 1.0
    if x not in graph or y not in graph:  return -1.0
    queue = collections.deque()
    queue.append((a,1.0))    # record visited vetex, avoid circle
    while queue:
        first, cur_val = queue.popleft()
        if first == y:  # the end condition, return when the first node reach the second.
            return cur_val
        visited.add(first)

    for neighbor, value in graph[first]:  # Traverse all neighbor of graph[first] node, bfs
        if neighbor not in visited:
            queue.append((neighbor,cur_val*value))

    return -1.0





