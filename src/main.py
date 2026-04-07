from structures import *

list = List()
tree = ABR()

values = [30, 10, 50, 20, 5, 40]
print(f"Values: {values}")

for v in values:
    list.insert(v)
    tree.insert(v)

print("\nList: ")
print("-> ".join(list.getAll()) + " -> None")

print("\nTree: ")
tree.printInorder(tree.root)