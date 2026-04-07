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

# ------------------------