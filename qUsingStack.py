class Queue(object):
    def __init__(self):
        """
        initialize your data structure here with 2 stacks
        """
        self.enq = []
        self.deq = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.enq.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.deq.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.deq[-1]# the element on the top of deq

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.deq) and (not self.enq) # will return true only if both are empty! (if not empty: return false)

    def move(self):
        """
        rtype: nothing 把enq pop 的東西移進 deq (move enq into deq when deq is empty)
        """
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
