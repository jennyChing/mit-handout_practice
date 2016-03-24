class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        #sort reversively
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        #recover q1 and q2
        self.q1 = self.q2
        self.q2 = []

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
    def empty(self):
        """
        :rtype: bool
        """
        return self.q1

if __name__ == '__main__':
    s=Stack()
    s.push(1)
    assert s.top()==1, "Stack is empty"
    s.push(4)
    s.push(3)
    s.push(2)

