# Subarray with Given Sum
# naive

def issubsum(arr, target_sum):
    s, curr = 0, 0
    for i in range(len(arr)):
        curr += arr[i]

        # Shrink the window if the current sum exceeds the target sum
        while curr > target_sum and s <= i:
            curr -= arr[s]
            s += 1

        # If the current sum matches the target sum, return True
        if curr == target_sum:
            return True

    # If no subarray is found with the given sum, return False
    return False


arr = [1,2,3,4,5,1]
sum = 6
print(issubsum(arr, sum))
