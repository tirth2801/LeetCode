class MyQueue:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        :rtype: nothing
        """
        self.move()
        # self.outStack.pop()
        return self.outStack.pop()

    def peek(self) -> int:
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)
    
    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()