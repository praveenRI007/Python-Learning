class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def height_of_tree(root):
    if root is None:
        return 0

    else:
        return max(height_of_tree(root.right) , height_of_tree(root.left)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

print(height_of_tree(root))
