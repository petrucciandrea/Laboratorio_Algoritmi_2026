# LISTA ORDINATA

class Item:    
    def __init__(self, k):
        self.key = k
        self.next = None
        
    def __str__(self):
        return str(self.key)
    
class List:
    def __init__(self): # Empty list
        self.root = None

    def insert(self,value):
        y = Item(value)
        if self.root is None or y.key < self.root.key:
            y.next = self.root
            self.root = y
        else:
            x = self.root
            while x.next is not None and x.next.key < y.key:
                x = x.next
            y.next = x.next
            x.next = y

    def getAll(self):
        x = self.root
        ret = []
        while x is not None:
            ret.append(str(x.key))
            x = x.next
        return(ret)

    def select(self,i):
        x = self.root
        for _ in range(i - 1):
            if x is None:
                return None 
            x = x.next
        return x
    
    def search(self, k):
        x = self.root
        while x is not None and x.key <= k:
            if x.key == k:
                return x
            x = x.next
        return None

    def delete(self, k):
        if self.root is None:
            return
        if self.root.key == k:
            self.root = self.root.next
            return
        x = self.root
        while x.next is not None and x.next.key <= k:
            if x.next.key == k:
                x.next = x.next.next
                return
            x = x.next

# ------------------------


# ALBERI BINARI DI RICERCA

class Node:
    def __init__(self, k):
        self.key = k
        self.p = None
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.key)

class ABR:
    def __init__(self): # Empty tree
        self.root = None

    def insert(self,value):
        z = Node(value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def printPreorder(self,x):
        if x is not None:
            self.printPreorder(x.left)
            self.printPreorder(x.right)
            print(x.key)

    def printInorder(self,x):
        if x is not None:
            self.printInorder(x.left)
            print(x.key)
            self.printInorder(x.right)

    def printPostorder(self,x):
        if x is not None:
            print(x.key)
            self.printPostorder(x.left)
            self.printPostorder(x.right)

    def select(self,x,i):
        if x is None:
            return None
        left_size = x.left.size if x.left is not None else 0
        r = left_size + 1
        if i == r:
            return x
        elif i < r:
            return self.select(x.left, i)
        else:
            return self.select(x.right, i - r)
    
    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x 

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x
    
    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def switch(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self, z):
        if z is None:
            return
        if z.left is None:
            self.switch(z, z.right)            
        elif z.right is None:
            self.switch(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.switch(y, y.right)
                y.right = z.right
                y.right.p = y
            self.switch(z, y)
            y.left = z.left
            y.left.p = y

# ------------------------