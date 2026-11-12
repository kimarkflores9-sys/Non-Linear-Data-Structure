from collections import deque

# Create Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Breadth-First Search (BFS)
def BFS(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Depth-First Search (DFS) - Preorder
def DFS(root):
    if root is None:
        return

    print(root.data, end=" ")
    DFS(root.left)
    DFS(root.right)


# Main Program
if __name__ == "__main__":

    # Create Binary Tree
    root = Node('F')

    root.left = Node('L')
    root.right = Node('O')

    root.left.left = Node('R')
    root.left.right = Node('E')

    root.right.left = Node('S')

    # Display BFS
    print("BFS Traversal:")
    BFS(root)

    # Display DFS
    print("\n\nDFS Traversal:")
    DFS(root)

    print()