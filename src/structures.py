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
        stack = []
        count = 0
        while stack or x is not None:
            if x is not None:
                stack.append(x)
                x = x.left
            else:
                x = stack.pop()
                count += 1
                if count == i:
                    return x
                x = x.right
        return None
    
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

# ALBERI AVL

class AVLNode(Node):
    def __init__(self, k):
        super().__init__(k) 
        self.height = 1
        self.size = 1

class AVL(ABR):
    def __init__(self):
        super().__init__()

    def get_height(self, x):
        if x is None:
            return 0
        return x.height

    def get_size(self, x):
        if x is None:
            return 0
        return x.size

    def get_balance(self, x):
        if x is None:
            return 0
        return self.get_height(x.left) - self.get_height(x.right)

    def _update_node(self, x):
        if x is not None:
            x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
            x.size = 1 + self.get_size(x.left) + self.get_size(x.right)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        self._update_node(x)
        self._update_node(y)

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.p = y
        x.p = y.p
        if y.p is None:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
        self._update_node(y)
        self._update_node(x)

    def _balance_up(self, node):
        curr = node
        while curr is not None:
            self._update_node(curr)
            balance = self.get_balance(curr)
            if balance > 1 and self.get_balance(curr.left) >= 0:
                self.right_rotate(curr)
            elif balance > 1 and self.get_balance(curr.left) < 0:
                self.left_rotate(curr.left)
                self.right_rotate(curr)
            elif balance < -1 and self.get_balance(curr.right) <= 0:
                self.left_rotate(curr)
            elif balance < -1 and self.get_balance(curr.right) > 0:
                self.right_rotate(curr.right)
                self.left_rotate(curr)
            curr = curr.p

    def insert(self, value):
        z = AVLNode(value)
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
        self._balance_up(z)

    def delete(self, z):
        if z is None:
            return
        balance_start = None        
        if z.left is None:
            balance_start = z.p
            self.switch(z, z.right)            
        elif z.right is None:
            balance_start = z.p
            self.switch(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                balance_start = y.p
                self.switch(y, y.right)
                y.right = z.right
                y.right.p = y
            else:
                balance_start = y
            self.switch(z, y)
            y.left = z.left
            y.left.p = y
        if balance_start is not None:
            self._balance_up(balance_start)
    
    def select(self, i):
        """Metodo pubblico per cercare l'i-esimo elemento"""
        return self._os_select(self.root, i)

    def _os_select(self, x, i):
        """Logica ricorsiva Order-Statistic Select"""
        if x is None:
            return None            
        left_size = self.get_size(x.left)
        r = left_size + 1
        if i == r:
            return x
        elif i < r:
            return self._os_select(x.left, i)
        else:
            return self._os_select(x.right, i - r)

#-------------------------