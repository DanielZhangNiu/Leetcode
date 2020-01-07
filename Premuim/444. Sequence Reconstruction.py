"""
    Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

    Example 1:

    Input:
    org: [1,2,3], seqs: [[1,2],[1,3]]

    Output:
    false

    Explanation:
    [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
    Example 2:

    Input:
    org: [1,2,3], seqs: [[1,2]]

    Output:
    false

    Explanation:
    The reconstructed sequence can only be [1,2].
    Example 3:

    Input:
    org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

    Output:
    true

    Explanation:
    The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
    Example 4:

    Input:
    org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

    Output:
    true
    UPDATE (2017/1/8):
    The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.


"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs: return False
        degree = collections.defaultdict(int)
        children = collections.defaultdict(list)
        for seq in seqs:
            if not seq:continue
            degree[seq[0]]+=0
            for i in range(len(seq)-1):
                children[seq[i]].append(seq[i+1])
                degree[seq[i+1]]+=1

        queue = collections.deque([ i for i in degree if degree[i] == 0])
        
        if len(queue) > 1: return False
        res = []
        
        while len(queue) == 1:
            cur = queue.popleft()
            res.append(cur)
            for nxt in children[cur]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    queue.append(nxt)
        if len(queue) > 1: return False
        
        return org == res and len(set(degree.keys()))==len(org)
            
        
