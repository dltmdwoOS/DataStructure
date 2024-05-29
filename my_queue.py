import exception
import node
import stack

class queue_array():
    def __init__(self, N):
        self.Q = [None]*N
        self.N = N
        self.f = 0
        self.r = N-1
        
    def size(self):
        return (self.N + self.r - self.f + 1)%self.N
    
    def isEmpty(self):
        return self.size() == 0 ## (r + 1 (+ N))%N == f
    def isFull(self):
        return self.size() == self.N - 1 ## (r + 2 (+ N))%N == f
    
    def enqueue(self, e):
        if self.isFull():
            exception.FullQueueException()
        self.r = (self.r + 1)%self.N # r 증가
        self.Q[self.r] = e
        
    def dequeue(self):
        if self.isEmpty():
            exception.EmptyQueueException()
        e = self.Q[self.f]
        self.f = (self.f + 1)%self.N # f 증가
        return e
    
    def front(self):
        if self.isEmpty():
            exception.EmptyQueueException()
        return self.Q[self.f]
        
        
class queue_SLL():
    def __init__(self) -> None:
        self.f = None
        self.r = None
        
    def isEmpty(self):
        return self.f == None
    
    def enqueue(self, e):
        new_node = node.SingleNode(e) # constructor : new_node.next == None, new_node.data == e
        if self.isEmpty():
            self.f = self.r = new_node
        else:
            self.r.next = new_node
            self.r = self.r.next
            
    def dequeue(self):
        if self.isEmpty():
            raise exception.EmptyQueueException()
        e = self.f.data
        self.f = self.f.next
        if (self.f == None):
            self.r = None
        return e
    
    
class deque_array():
    def __init__(self) -> None:
        pass
            
        
class queue_stack():
    def __init__(self) -> None:
        self.stack1 = stack.Stack_array(100)
        self.stack2 = stack.Stack_array(100)
        
    def enqueue(self, e):
        self.stack1.push(e)
        
    def dequeue(self):
        if self.isEmpty():
            exception.EmptyQueueException()
        if self.stack2.isEmpty():
            while (not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    