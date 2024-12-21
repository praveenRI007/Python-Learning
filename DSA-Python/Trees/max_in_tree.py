class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def max_of_tree(root):
    if root is None:
        return 0

    else:
        return max(root.data, max_of_tree(root.right), max_of_tree(root.left))


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(10)
root.left.right = Node(5)

print(max_of_tree(root))
