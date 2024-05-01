import exception
import node

# 배열 기반 List ADT
class List_array():
  def __init__(self, length):
    self.length = length
    self.elem = [None]*length
    self.size = 0

  # 일반 메소드
  def traverse(self):
    for i in range(self.size):
      print(self.elem[i])

  # 접근 메소드
  def get(self, r):
    if r > self.size-1 or r < 0:
       raise exception.InvalidRankException()
    return self.elem[r]

  # 갱신 메소드
  def set(self, r, e):
    if r > self.size-1 or r < 0:
      raise exception.InvalidRankException()
    self.elem[r] = e

  def add(self, r, e):
    if self.size == self.length:
      raise exception.FullListException()
    if r > self.size or r < 0:
      raise exception.InvalidRankException()

    for i in range(self.size-1, r-1, -1):
      self.elem[i+1] = self.elem[i]
    self.elem[r] = e
    self.size += 1

  def addFirst(self, e):
    self.add(0, e)

  def addLast(self, e):
    self.add(self.size, e)

  def remove(self, r):
    if r > self.size-1 or r < 0:
      raise exception.InvalidRankException()

    e = self.elem[r]
    for i in range(r+1, self.size):
      self.elem[i-1] = self.elem[i]
    self.size -= 1
    return e

  def removeFirst(self):
    return self.remove(0)

  def removeLast(self):
    return self.remove(self.size-1)

# Doubly Linked List based List ADT
class List_DLL():
  value = 50
  def __init__(self):
    self.head = node.DoubleNode('header')
    self.tail = node.DoubleNode('trailer')
    self.head.next = self.tail
    self.tail.prev = self.head
    self.size = 0

  def isEmpty(self):
    if (self.size == 0):
      return True
    return False

  def get(self, r) -> int: # get node's data
    p = self.head
    for i in range(r):
      p = p.next
    return p.data

  def traverse(self):
    p = self.head.next
    while(p != self.tail):
      print(p.data)
      p = p.next

  def addNodeBefore(self, p, e):
    q = node.DoubleNode(e) # 추가하고 싶은 대상
    q.prev = p.prev
    q.next = p
    p.prev.next = q
    p.prev = q

  def add(self, r, e):
    if r > self.size+1 or r < 1:
      raise exception.InvalidRankException()

    p = self.head
    for i in range(r):
      p = p.next
    self.addNodeBefore(p, e)
    self.size += 1

  def addFirst(self, e):
    self.add(1, e)

  def addLast(self, e):
    self.add(self.size+1, e)

  def removeNode(self, p):
    p.prev.next = p.next
    p.next.prev = p.prev

  def remove(self, r):
    if r > self.size or r < 1:
      raise exception.InvalidRankException()

    p = self.head
    for i in range(r):
      p = p.next
    e = p.data
    self.removeNode(p)
    self.size -= 1
    return e

  def removeFirst(self):
    return self.remove(1)

  def removeLast(self):
    return self.remove(self.size)