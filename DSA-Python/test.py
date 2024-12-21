# User function Template for python3


'''class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None'''


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):
        # code here
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        print(left_height)
        print(right_height)

        if abs(left_height - right_height) <= 1:
            return True
        else:
            return False

    def height_of_tree(self, root):
        if root is None:
            return 0

        else:
            return max(self.height_of_tree(root.right), self.height_of_tree(root.left)) + 1


# {
# Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while q and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
        i += 1
    return root


# Main driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        if ob.isBalanced(root):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends