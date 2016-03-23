class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.min_stack[-1] == self.stack.pop():
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

if __name__ == '__main__':
    s = MinStack()
    s.push(5)
    assert s.top()==5, "The top element should be %r" % s.top()
    assert s.getMin()==5, "The min element should be %r" % s.getMin()
    s.push(6)
    s.push(4)
    assert s.getMin()==4, "The min element should be %r" % s.getMin()
    s.push(2)
    assert s.getMin()==2, "The min element should be %r" % s.getMin()
    s.pop()
    assert s.getMin()==4, "The min element should be %r" % s.getMin()
    s.pop()
    assert s.getMin()==5, "The min element should be %r" % s.getMin()

