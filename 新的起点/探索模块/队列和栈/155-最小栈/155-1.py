class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 借助辅助栈
        # 345222111
        # 333222111
        
        self.stack1=[]
        self.stack2=[]
        self.head1,self.head2=-1,-1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.head1+=1
        self.head2+=1
        self.stack1.append(x)
        if self.head1==0:
            self.stack2.append(x)
        else:
            if self.stack2[self.head2-1]>x:
                self.stack2.append(x)
            else:
                self.stack2.append(self.stack2[self.head2-1])
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack1.pop()
        self.stack2.pop()
        self.head1-=1
        self.head2-=1

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[self.head1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[self.head2]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()