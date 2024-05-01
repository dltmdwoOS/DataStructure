import exception

class circular_array():
  def __init__(self, N):
    self.N = N
    self.f = 0
    self.l = -1
    self.elem = [None]*N

  # 일반 메소드
  def traverse(self):
    for i in range(self.f, self.l+1):
      print(self.elem[i])

  def size(self):
      return (self.l + self.N - self.f + 1) % self.N
  
  # 접근 메소드
  def get(self, r):
    if r >= self.size() or r < 0:
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
