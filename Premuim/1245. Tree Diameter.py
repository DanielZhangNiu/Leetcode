"""
 Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

 The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

  

 Example 1:



 Input: edges = [[0,1],[0,2]]
 Output: 2
 Explanation:
 A longest path of the tree is the path 1 - 0 - 2.
 Example 2:



 Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
 Output: 4
 Explanation:
 A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
  

 Constraints:

 0 <= edges.length < 10^4
 edges[i][0] != edges[i][1]
 0 <= edges[i][j] <= edges.length
 The given edges form an undirected tree.

"""
class Solution:
  def treeDiameter(self, edges: List[List[int]]) -> int:
      if not edges: return 0
      # tree is special graph, there are leaf node, so the longest path should start from leafnode
      table = collections.defaultdict(list)
      for edge in edges:
          u , v = edge
          table[u].append(v)
          table[v].append(u)
      
      candidate = set((node,None) for node in table if len(table[node]) == 1 )
      
      move = 0
      while candidate:
          new_can = set()
          print(candidate)
          for node, pre in candidate:
              for neighbor in table[node]:
                  if neighbor != pre:
                      new_can.add((neighbor, node))
                      
          candidate, move = new_can, move + 1
                                
      return max(move - 1, 0)
