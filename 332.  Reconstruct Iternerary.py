"""
    Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
    
    Note:
    
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    Example 1:
    
    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
    Example 2:
    
    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
    But it is larger in lexical order.

"""
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    
    # Greedy: sort children  + postorder traversal
    """
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    trips = {JFK:[ATL,SFO], ATL:[JFK,SFO], SFO:[ATL]}
    every dfs will remove the first destination from the current start, after there is no flight left,
    the SFO in this example (trips[SFO] == None, then start to append start to res), add this destiantion into result, at the last, return the reversed list
    """
    if not tickets: return []
            
    # build the trip graph
    trips = collections.defaultdict(list)
    for start, end in tickets:
        trips[start].append(end)
                    
    for i,pair in trips.items():
        pair.sort()
    # recursion
    res = []
    self.dfs(trips, 'JFK', res)
    return res[::-1]

def dfs(self, trips, start, res):
    destinations = trips[start]
    while len(destinations) > 0:
        dest = destinations.pop(0)
        self.dfs(trips, dest, res)
    res.append(start)



    """
    if not tickets: return []
    totallen = len(tickets) + 1
            
    trips = {}
    for pair in tickets:
        if pair[0] not in trips:
            trips[pair[0]] = []
            
        trips[pair[0]].append(pair[1])
            
    for key,pair in trips.items():
        pair.sort()
            
    start = "JFK"
    res = []
    res.append(start)
            
            
    if self.DFS(start, res,trips, totallen):
        return res
    return None
            
    def DFS(self,start, path, trips, totallen):
        if len(path) == totallen:
            return True
        if start not in trips:
            return False
            
        destinations = trips.get(start)
            
        for i in range(len(destinations)):
            dest = destinations[i]
            print(dest,i)
            destinations.pop(i)
            path.append(dest)
            if self.DFS(dest,path, trips, totallen):
                return True
            
            path.pop()
            destinations.insert(i,dest)
            
        return False
            """
