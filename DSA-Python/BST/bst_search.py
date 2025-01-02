class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root


def search_bst(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search_bst(root.right, key)

    return search_bst(root.left, key)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print(search_bst(r, 40))
print(search_bst(r, 0))

# O(h) time complexity where h is the height of the given BST.
