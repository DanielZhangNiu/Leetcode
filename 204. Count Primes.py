"""
    Count the number of prime numbers less than a non-negative number, n.
    
    Example:
    
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
   
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def countPrimes(n):
    if n < 3:
        return 0
    prime = [True] * n
    prime[1] = prime[0] = False
        
    for i in range(2, int(n**0.5)+1):
        if prime[i] == True:
            for j in range(2, (n-1)//(j+1)):
                prime[i*j] = False
    return sum(prime)
