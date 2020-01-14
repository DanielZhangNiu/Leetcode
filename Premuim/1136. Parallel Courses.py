"""
 There are N courses, labelled from 1 to N.

 We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

 In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

 Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

  

 Example 1:



 Input: N = 3, relations = [[1,3],[2,3]]
 Output: 2
 Explanation:
 In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
 Example 2:



 Input: N = 3, relations = [[1,2],[2,3],[3,1]]
 Output: -1
 Explanation:
 No course can be studied because they depend on each other.
  

 Note:

 1 <= N <= 5000
 1 <= relations.length <= 5000
 relations[i][0] != relations[i][1]
 There are no repeated relations in the input.
"""
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        
        if not relations: return -1
        degree = [0] * (N+1)
        degree[0] = 1
        next = collections.defaultdict(list)
        for x, y in relations:
            degree[y] += 1
            next[x].append(y)
        
        available = [ i for i, count in enumerate(degree) if count == 0]
        
        res = 0
        while available:
            newQ = []
            for _ in range(len(available)):
                nextcourse = available.pop()
                for course in next[nextcourse]:
                    degree[course] -= 1
                    if not degree[course]:
                        newQ.append(course)
            
            res += 1
            available = newQ
            
        return res if sum(degree[1:]) == 0 else -1
