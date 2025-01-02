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


"""This function is used to find floor of a key"""


def floor(root, key):
    if (not root):
        return INT_MAX

    """ If root.data is equal to key """
    if (root.data == key):
        return root.data

    """ If root.data is greater than the key """
    if (root.data > key):
        return floor(root.left, key)

    """ Else, the floor may lie in right subtree 
    or may be equal to the root"""
    floorValue = floor(root.right, key)
    return floorValue if (floorValue <= key) else root.data


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
    print(floor(root, 9))
