# Python3 program to find the minimum
# group flips in a binary array

def printGroups(arr, n):
    # Traverse through all array elements
    # starting from the second element
    for i in range(1, n):

        # If current element is not same
        # as previous
        if (arr[i] != arr[i - 1]):

            # If it is same as first element
            # then it is starting of the interval
            # to be flipped.
            if (arr[i] != arr[0]):
                print("From", i, "to ", end="")

            # If it is not same as previous
            # and same as the first element, then
            # previous element is end of interval
            else:
                print(i - 1)

    # Explicitly handling the end of
    # last interval
    if (arr[n - 1] != arr[0]):
        print(n - 1)


# Driver Code
if __name__ == '__main__':
    arr = [0, 1, 1, 0, 0, 0, 1, 1]
    n = len(arr)

    printGroups(arr, n)