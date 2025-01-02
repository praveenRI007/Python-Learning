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


def deleteNode(root, key):
    if root == None:
        return None

    if root.val > key:
        root.left = deleteNode(root.left, key)

    elif root.val < key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = get_succ(root.right, key)
            root.val = succ
            root.right = deleteNode(root.right, succ)

    return root


def get_succ(curr, key):
    while curr.left is not None:
        curr = curr.left

    return curr.val


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("before deletion:")
inorder(r)

deleteNode(r,60)

print("after deletion:")
inorder(r)
