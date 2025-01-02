def maxIndexDiff(arr):
    # code here
    max_diff = float('-inf')

    i = 0
    j = len(arr) - 1

    while i <= j:

        print(i, j)

        if arr[i] >= arr[j]:
            j -= 1
            continue

        if arr[i] <= arr[j]:
            max_diff = max(max_diff, j - i)

    return max_diff


maxIndexDiff([1,10])