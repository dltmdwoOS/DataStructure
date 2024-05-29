from my_queue import queue_SLL

class binary_node():
    def __init__(self, e):
        self.parent = None
        self.left = None
        self.right = None
        self.elem = e
        
class binary_tree():
    def __init__(self,r):
        self.root = binary_node(r)
    
    def parent(self, v):
        return v.parent
    
    def isExternal(self, v):
        return v.left == None and v.right == None
    
    def isInternal(self, v):
        return not self.isExternal(v)
    
    def isRoot(self, v):
        return v.parent == None
    
    def depth(self, v):
        if self.isRoot(v):
            return 0
        else:
            return 1 + self.depth(self.parent(v))
    
    def height(self, v):
        if self.isExternal(v):
            return 0
        else:
            hl = self.height(v.left) 
            hr = self.height(v.right)
            return hl+1 if hl >= hr else hr+1
        

    def preOrder(self, v):
        print(v.elem)
        if v.left != None:
            self.preOrder(v.left)
        if v.right != None:
            self.preOrder(v.right)
            
    def postOrder(self, v):
        if v.left != None:
            self.postOrder(v.left)
        if v.right != None:
            self.postOrder(v.right)
        print(v.elem)
        
    def levelOrder(self, v):
        Q = queue_SLL()
        Q.enqueue(v)
        while(not Q.isEmpty()):
            v = Q.dequeue()
            print(v.elem)
            Q.enqueue(v.left)
            Q.enqueue(v.right)
            