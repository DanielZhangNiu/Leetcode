"""
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    Example:
    
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

"""


# Two stack, push at the same time, but minstack only push smallest value in.
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            self.minstack.append(min(self.minstack[-1], x))
    # @return nothing
def pop(self):
    self.stack.pop()
    self.minstack.pop()
    # @return an integer
    def top(self):
        return self.stack[-1]
    
    # @return an integer
    def getMin(self):
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
