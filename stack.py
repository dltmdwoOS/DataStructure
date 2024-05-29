import node
import exception
import my_queue

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
    

class MultiStack_1DArray():
    def __init__(self, N, n):
        self.stack = [None]*N
        self.N = N
        self.n = n
        self.stackSize = N // n # MaxSize of each Stack 
        self.b = [i for i in range(-1, N, n)] # Base Index Array
        self.t = [i for i in range(-1, N-n, n)] # Top Index Array
        
    def size(self, i): # Size of Stack(i)
        return self.t[i] - self.b[i]

    def isEmpty(self, i): # isEmpty of Stack(i)        
        return self.b[i] == self.t[i]
    
    def isFull(self, i):
        return self.t[i] == self.b[i+1]
    
    def top(self, i):
        if self.isEmpty(i):
            raise exception.EmptyStackException()
        return self.stack[self.t[i]]
    
    def traverse(self, i):
        if i > self.n:
            raise exception.InvalidIndexException()
        if self.isEmpty(i):
            raise exception.EmptyStackException()
        
        index = self.b[i]
        while(index != self.t[i]):
            index += 1
            print(self.stack[index])
            
            
    def add(self, i, e): # Stack(i)에 e 추가
        if i > self.n:
            raise exception.InvalidIndexException()
        if self.isFull(i):
            raise exception.FullStackException()
        
        self.t[i] += 1
        self.stack[self.t[i]] = e
        
    def pop(self, i): # Stack(i)의 top element pop
        if i > self.n:
            raise exception.InvalidIndexException()
        if self.isEmpty(i):
            raise exception.EmptyStackException()
        
        e = self.stack[self.t[i]]
        self.t[i] -= 1
        return e
        
    
class stack_queue():
    def __init__(self) -> None:
        self.queue1 = my_queue.queue_SLL()
        self.queue2 = my_queue.queue_SLL()
        
    def push(self, e):
        self.queue1.enqueue(e)
    
    def pop(self):
        if self.queue1.isEmpty():
            exception.EmptyStackException()
        e = None
        while(1):
            e = self.queue1.dequeue()
            if self.queue1.isEmpty():
                break
            self.queue2.enqueue(e)
        while(not self.queue2.isEmpty()):
            self.queue1.enqueue(self.queue2.dequeue())
        return e