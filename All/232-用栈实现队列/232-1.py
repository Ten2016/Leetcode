class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 建立循环队列
        self.size=100
        self.queue=[0 for _ in range(self.size)]
        self.front=self.rear=-1

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=x
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.front=(self.front+1)%self.size
        return self.queue[self.front]
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[self.front+1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.front==self.rear


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()