# Import the heap functions from python library
from heapq import heappush, heappop, heapify


# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2  # Corrected to integer division

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)  # Using heapq's heappush to insert new key

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)  # Update index to move up the heap

    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)  # Using heapq's heappop to extract the minimum

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))  # Decrease the key to negative infinity
        self.extractMin()  # Extract the minimum (which is now the element to delete)

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0] if self.heap else None  # Safely handle empty heap


# Driver program to test the above functions
heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)  # Deletes element at index 1 (indexing starts from 0)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin())  # Prints the minimum element
print(heapObj.getMin())  # Prints the current minimum element after extraction
heapObj.decreaseKey(2, 1)  # Decreases value at index 2 to 1
print(heapObj.getMin())  # Prints the updated minimum element
