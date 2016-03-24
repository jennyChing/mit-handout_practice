class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)
        print("push",self.q1)

    def pop(self):
        """
        :rtype: nothing
        """
        #sort reversively
        n = len(self.q1)
        while n > 1:
            n -= 1
            self.q1.append(self.q1.pop(0))
            print("while",self.q1)
        self.q1.pop(0)
        print("pop",self.q1)

    def top(self):
        """
        :rtype: int
        """
        n = len(self.q1)
        while n > 1:
            n -= 1
            self.q1.append(self.q1.pop(0))
            print("while",self.q1)
        return self.q1[0]
    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1

if __name__ == '__main__':
    s=Stack()
    s.push(1)
    assert s.top()==1, "Stack is empty"
    s.push(4)
    assert s.top()==4, "Stack is empty"
    s.pop()
    assert s.top()==1, "Stack is empty"
    s.push(3)
    assert s.empty()==False, "Stack is empty"
    s.push(2)

