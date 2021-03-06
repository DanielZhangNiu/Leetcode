"""
    A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

    Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

    Note:

    A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
    Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
    Example 1:

    Input:
    [[0,1,10], [2,0,5]]

    Output:
    2

    Explanation:
    Person #0 gave person #1 $10.
    Person #2 gave person #0 $5.

    Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
    Example 2:

    Input:
    [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

    Output:
    1

    Explanation:
    Person #0 gave person #1 $10.
    Person #1 gave person #0 $1.
    Person #1 gave person #2 $5.
    Person #2 gave person #0 $5.

    Therefore, person #1 only need to give person #0 $4, and all debt is settled.
"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()
            # q store ([index set], sum of set)
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        bal_cnt = len(non_zero)
        
        while len(non_zero) > 0:
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt
        
