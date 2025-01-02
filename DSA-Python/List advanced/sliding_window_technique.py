# Sliding Window Technique
# Efficient

def maxsum(arr, k):
    curr = 0
    for i in range(k):
        curr += arr[i]
    res = curr
    for i in range(k, len(arr)):
        curr = curr + arr[i] - arr[i - k]
        res = max(res, curr)

    return res


arr = [1, 8, 30, -5, 20, 7]
k = 4
print(maxsum(arr, k))
