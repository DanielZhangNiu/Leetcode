"""
 You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.

 You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

 Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.

 If there isn't such day, return -1.

  

 Example 1:

 Input:
 bulbs: [1,3,2]
 K: 1
 Output: 2
 Explanation:
 On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
 On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
 On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
 We return 2 because on the second day, there were two on bulbs with one off bulb between them.
 Example 2:

 Input:
 bulbs: [1,2,3]
 K: 1
 Output: -1
  

 Note:

 1 <= N <= 20000
 1 <= bulbs[i] <= N
 bulbs is a permutation of numbers from 1 to N.
 0 <= K <= 20000

"""
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers:
            return -1
        
        def helper(day,start,k,maxV):
            for i in range(start,start + k):
                if day[i] < maxV:
                    return False
            return True
        
        day = [0] * len(flowers)
        for i in range(0,len(flowers)):
            idx = flowers[i]-1
            day[idx] = i+1
            
        cnt = float('inf')
        for j in range(k+1,len(flowers)):
            maxV = max(day[j-k-1],day[j])
            if helper(day,j-k,k,maxV):
                cnt = min(cnt,maxV)
              
        return cnt if cnt!=float('inf') else -1
