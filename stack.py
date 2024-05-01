import node
import exception

class Stack_array():
    def __init__(self, N):
        self.stack = [None]*N
        self.N = N
        self.t = -1
        
    def push(self, e):
        if self.t == self.N - 1:
            raise exception.FullStackException()
        
        self.t += 1
        self.stack[self.t] = e
        
    def pop(self):
        if self.isEmpty():
            raise exception.EmptyStackException()
        self.t -= 1
        return self.stack[self.t+1]
    
    def top(self):
        if self.isEmpty():
            raise exception.EmptyStackException()
        return self.stack[self.t]
    
    def size(self):
        return self.t + 1
    
    def isEmpty(self):
        return self.t == -1
    
    def traverse(self):
        if self.isEmpty():
            raise exception.EmptyStackException()
        for i in range(self.t + 1):
            print(self.stack[i])
    