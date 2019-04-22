"""
    Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
    
    Calling next() will return the next smallest number in the BST.
    
    
    
    Example:
    

    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // return 3
    iterator.next();    // return 7
    iterator.hasNext(); // return true
    iterator.next();    // return 9
    iterator.hasNext(); // return true
    iterator.next();    // return 15
    iterator.hasNext(); // return true
    iterator.next();    // return 20
    iterator.hasNext(); // return false
    
    
    Note:
    
    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


"""
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q=[]
        self.allLeftIntoStack(root)
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True
    
    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        self.allLeftIntoStack(cur.right)
        return cur.val
    
    def allLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
