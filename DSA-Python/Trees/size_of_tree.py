class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def size_of_tree(root):
    if root is None:
        return 0

    else:
        return size_of_tree(root.right) + 1 + size_of_tree(root.left)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

print(size_of_tree(root))
