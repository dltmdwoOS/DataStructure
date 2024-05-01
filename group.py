import exception
import list
import node


# 설계방안 A : 레코드의 리스트(array 예시) 이용
class Group_array(list.List_array):
    def __init__(self, length):
        self.length = length
        self.elem = [None]*length
        self.group = [None]*length
        self.size = 0
        
    def traverseGroup(self, g):
      for i in range(self.size):
          if self.group[i] == g:
              print(self.elem[i])
              
    def set(self, r, e, g):
        if r > self.size-1 or r < 0:
            raise exception.InvalidRankException()
        self.elem[r] = e
        self.group[r] = g
        
    def add(self, r, e, g):
        if self.size == self.length:
            raise exception.FullListException()
        if r > self.size or r < 0:
            raise exception.InvalidRankException()
        
        for i in range(self.size-1, r-1, -1):
            self.elem[i+1] = self.elem[i]
            self.group[i+1] = self.group[i]
        self.elem[r] = e
        self.group[r] = g
        self.size += 1
            
    def addFirst(self, e, g):
        self.add(0, e, g)

    def addLast(self, e, g):
        self.add(self.size, e, g)
        
    def removeGroup(self, g):
        i = 0
        while(True):
            if self.group[i] == g:
                self.remove(i)
            else:
                i += 1
                
# 설계방안 B1 : 부리스트(배열)의 리스트(배열) 이용
pass

# 설계방안 B2 : 부리스트(연결리스트)의 리스트(배열) 이용
class Group2_DLL():
    def __init__(self, length):
        self.length = length
        self.groups = [node.DoubleNode(f'header{i}') for i in range(length)]
    
    def traverseGroup(self, g):
        head = self.groups[g].next
        while(head != None):
            print(head.data)
            head = head.next
    
    def addElementLast(self, e, g):
        new_node = node.DoubleNode(e)
        head = self.groups[g]
        while (head.next != None):
            head = head.next
        head.next = new_node
        new_node.prev = head