class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node, result):
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)

# Build the tree (Assessment 3.5)
root = Node("K")
root.left = Node("I")
root.right = Node("M")

root.left.left = Node("A")
root.left.right = Node("R")
root.left.left.left = Node("L")
root.left.left.right = Node("O")
root.left.right.left = Node("R")
root.left.right.right = Node("E")

root.right.left = Node("K")
root.right.right = Node("F")
root.right.left.left = Node("S")

for name, func in [("Preorder", preorder),
                   ("Inorder", inorder),
                   ("Postorder", postorder)]:
    result = []
    func(root, result)
    print(f"{name}: {' -> '.join(result)}")