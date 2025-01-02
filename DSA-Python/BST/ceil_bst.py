# Python3 code to find floor of a key in BST
INT_MAX = 2147483647

# Binary Tree Node
""" A utility function to create a
new BST node """


class newNode:

    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" This function is used to insert 
new values in BST"""


def insert(root, key):
    if (not root):
        return newNode(key)
    if (key < root.data):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def getCeil(root, x):
    res = None

    while root != None:

        if root.data == x:
            return root.data
        elif root.data < x:
            root = root.right
        else:
            res = root
            root = root.left

    return res.data


# Driver Code
if __name__ == '__main__':
    # """ Let us create following BST
    #         7
    #         / \
    #     5     10
    #     / \ / \
    #     3 6 8 12 """
    root = None
    root = insert(root, 7)
    insert(root, 10)
    insert(root, 5)
    insert(root, 3)
    insert(root, 6)
    insert(root, 8)
    insert(root, 12)
    print(getCeil(root, 9))
