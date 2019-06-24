"""
    There are a total of n courses you have to take, labeled from 0 to n-1.
    
    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
    
    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    
    Example 1:
    
    Input: 2, [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.
    Example 2:
    
    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should
    also have finished course 1. So it is impossible.
    Note:
    
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

"""
def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
            
        Topological ordering
        if node v has not been visited, then mark it as 0.
        if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a cycle.
        if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no cycle contains v or its successors.
        """
    """
        graph = collections.defaultdict(list)
        visit = [0 for i in range(numCourses)]

        # build the prerequisites graph
        for x,y in prerequisites:
            graph[x].append(y)

        # status of visited: 0 unknown, 1 no cycle , -1 cycle
        def findcircle(visit, node):
            if visit[node] == -1:  # circle detected
                return False
            if visit[node] == 1:
                return True
            else:
                visit[node] = -1
                for neighbor in graph[node]:
                    if findcircle(visit,neighbor) == False:
                        return False
                visit[node] = 1
                return True

        for i in range(numCourses):
            if find_circle(i) == False:
                return False
        return True

    """
    num_count = [0 for _ in range(numCourses)]
    edgemap = collections.defaultdict(list)
    for c, pre in prerequisites:
        edgemap[pre].append(c)
        num_count[c] += 1

    available = [i for i,v in enumerate(num_count) if v == 0]

    where available:
        cur = available.pop()
        for neighbor in edgemap[cur]:
            num_count[neighbor] -= 1
            if num_count[neighbor] == 0:
                available.append(neighbor)

    return sum(num_count) == 0
            
