# O(n) solution in Python3 for finding
# maximum sum of a subarray of size k

# Returns maximum sum in
# a subarray of size k.

def maxSum(arr, n, k):
    if n < k:
        print("Invalid")
        return -1

    res = 0
    for i in range(0, n - k + 1):
        res = max(res, sum(arr[i:i + k]))

    return res


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
