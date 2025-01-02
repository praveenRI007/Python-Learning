# Python3 program to find the length of the
# longest alternating even odd subarray

# Function to find the longest subarray


def longestEvenOddSubarray(arr, n):
    # Length of longest
    # alternating subarray
    longest = 1
    cnt = 1

    # Iterate in the array
    for i in range(n - 1):

        # Increment count if consecutive
        # elements has an odd sum
        if ((arr[i] + arr[i + 1]) % 2 == 1):
            cnt = cnt + 1
        else:

            # Store maximum count in longest
            longest = max(longest, cnt)

            # Reinitialize cnt as 1 consecutive
            # elements does not have an odd sum
            cnt = 1

    # Length of 'longest' can never be 1 since
    # even odd has to occur in pair or more
    # so return 0 if longest = 1
    if (longest == 1):
        return 0

    return max(cnt, longest)


# Driver Code
arr = [1, 2, 3, 4, 5, 7, 8]

arr = [10,12,14,7,8]

n = len(arr)

print(longestEvenOddSubarray(arr, n))
