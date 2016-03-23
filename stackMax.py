class stack:
    def __init__(self):
        self.stack = []
        self.max_stack= []

    def push(self,x):
        self.stack.append(x)
        if  self.max_stack == [] or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        print(self.stack,self.max_stack)

    def pop(self):
        if self.max_stack[-1] == self.stack.pop():
            self.max_stack.pop()
        #self.stack.pop()
        print(self.stack,self.max_stack)

    def printMax(self):
        print("Max:",self.max_stack[-1])

if __name__ == "__main__":
    s = stack()
    s.push(4)
    s.push(3)
    s.push(5)
    s.push(5)
    s.push(5)
    s.push(5)
    s.pop()
    s.pop()
    s.printMax()
