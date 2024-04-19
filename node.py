

class SingleNode():
    def __init__(self, element):
        self.data = element
        self.next = None
    
class DoubleNode():
    def __init__(self, element):
        self.data = element
        self.prev = None
        self.next = None