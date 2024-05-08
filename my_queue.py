import exception

class queue_array():
    def __init__(self, N):
        self.Q = [None]*N
        self.N = N
        self.f = 0
        self.r = N-1
        
    def size(self):
        return (self.N + self.r - self.f + 1)%self.N
    
    def isEmpty(self):
        return self.size() == 0
    def isFull(self):
        return self.size() == self.N - 1
    
    def enqueue(self, e):
        if self.isFull():
            exception.FullQueueException()
        self.r = (self.r + 1)%self.N
        self.Q[self.r] = e
        
    def dequeue(self):
        if self.isEmpty():
            exception.EmptyQueueException()
        e = self.Q[self.f]
        self.f = (self.f + 1)%self.N
        return e
    
    def front(self):
        if self.isEmpty():
            exception.EmptyQueueException()
        return self.Q[self.f]
        
        