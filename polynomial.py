class polyNode():
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None
        
class poly():
    def __init__(self):
        self.head = polyNode('header', 'header')
        
    def printPoly(self):
        i = self.head.next
        while i != None:
            print(f"+ {i.coef}x^{i.exp}", end = ' ')
            i = i.next
            
    def appendTerm(self, coef, exp):
        new_term = polyNode(coef, exp)
        new_term.next = self.head.next # has to be first
        self.head.next = new_term   
    
    def addPoly(self, x, y):
        z = polyNode('header', 'header')
        i, j = x.head.next, y.head.next
        while i != None or j != None:
            if i.exp > j.exp:
                z.appendTerm(i.coef, i.exp)
                i = i.next
            elif i.exp < j.exp:
                z.appendTerm(j.coef, j.exp)
                j = j.next 
            else:
                z.appendTerm(i.coef+j.coef, i.exp)
                i, j = i.next, j.next 
        while i != None:
            z.appendTerm(i.coef, i.exp)
            i = i.next
        while j != None:
            z.appendTerm(j.coef, j.exp)
            j = j.next
        return z