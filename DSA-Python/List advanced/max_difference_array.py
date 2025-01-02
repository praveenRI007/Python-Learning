def max_diff(_arr, _n):
    res = arr[1] - arr[0]
    for i in range(0, _n - 1):
        for j in range(i + 1, _n):
            res = max(res, arr[j] - arr[i])

    return res


arr = [2, 3, 10, 6, 4, 8, 1]
n = len(arr)
print(max_diff(arr, n))

# Time Complexity : O(n^2)
# Auxiliary Space : O(1)


# Efficient  approach

def max_Abs_Diff(arr,n):
    min_ele = arr[0]
    max_ele = arr[1]

    for i in arr:
        min_ele = min(min_ele,i)
        max_ele = max(max_ele,i)

    return abs(min_ele - max_ele)


arr = [2, 1, 5, 3]
n = len(arr)
print(max_Abs_Diff(arr, n))


# Time Complexity : O(n)
#
# Auxiliary Space : O(1)