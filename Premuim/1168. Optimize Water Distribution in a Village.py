"""
 There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

 For each house i, we can either build a well inside it directly with cost wells[i], or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe. Connections are bidirectional.

 Find the minimum total cost to supply water to all houses.

  

 Example 1:



 Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
 Output: 3
 Explanation:
 The image shows the costs of connecting houses using pipes.
 The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
  

 Constraints:

 1 <= n <= 10000
 wells.length == n
 0 <= wells[i] <= 10^5
 1 <= pipes.length <= 10000
 1 <= pipes[i][0], pipes[i][1] <= n
 0 <= pipes[i][2] <= 10^5
 pipes[i][0] != pipes[i][1]


"""
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        if not wells or n == 0: return 0
        # construct wells to be virtual node connect with that villege
        villages = [0 for i in range(n*2)]
        
        # build graph:
        graph = collections.defaultdict(list)
        for n1,n2,weight in pipes:
            graph[n1].append((weight, n2))
            graph[n2].append((weight, n1))
            
        for idx,val in enumerate(wells):
            idx += 1
            village = idx + n
            graph[idx].append((val, village))
            graph[village].append((val,idx))
        
        minheap = []
        for vnode in range(n+1,n*2 + 1 ):
            villages[vnode -1] =  1
            for val, nxt in graph[vnode]:
                heapq.heappush(minheap, (val, nxt))
        
        res = 0
        # print(minheap )
        # print(graph)
        while minheap:
            weight,node = heapq.heappop(minheap)
            # print(cur)
            
            if villages[node-1] == 1:
                continue
            res += weight
            villages[node-1] = 1
            if sum(villages[:n]) == n:
                return res
            for val, nnode in graph[node]:
                if villages[nnode-1] == 0:
                    heapq.heappush(minheap, (val, nnode))
        return res
            
            
