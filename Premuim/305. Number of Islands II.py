"""
 A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 Example:

 Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
 Output: [1,1,2,3]
 Explanation:

 Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

 0 0 0
 0 0 0
 0 0 0
 Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

 1 0 0
 0 0 0   Number of islands = 1
 0 0 0
 Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

 1 1 0
 0 0 0   Number of islands = 1
 0 0 0
 Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

 1 1 0
 0 0 1   Number of islands = 2
 0 0 0
 Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

 1 1 0
 0 0 1   Number of islands = 3
 0 1 0
 Follow up:

 Can you do it in time complexity O(k log mn), where k is the length of the positions?


"""
class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        result = []
        parent = [-1]*m*n
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        self.num = 0
        for pos in positions:
            if tuple(pos) in visited:
                result.append(self.num)
                continue
            visited.add(tuple(pos))
            idx = pos[0]*n+pos[1]
            parent[idx] = idx
            self.num+=1
            for d in dirs:
                i =pos[0]+d[0]
                j = pos[1]+d[1]
                new_idx = i*n+j
                if i<0 or j<0 or i>=m or j>=n or parent[new_idx]==-1:
                    continue
                self.union(idx, new_idx, parent)
                
            result.append(self.num)
        return result

    def find(self, i, parent):
        if i!=parent[i]:
            parent[i]=self.find(parent[i], parent)
        return parent[i]
    
    def union(self, i,j, parent):
        root1 = self.find(i,parent)
        root2 = self.find(j, parent)
        if root1 != root2:
            parent[root1] = root2
            self.num -= 1
