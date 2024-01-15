import math

# Add any extra import statements you may need here
# Add any helper functions you may need here


def balancedSplitExists(arr):
# Write your code here

    arr = sorted(arr)
    total = sum(arr)

    if total%2 == 1: return False

    for i in range(len(arr)):
        if sum(arr[:i]) == total//2 and arr[i] > arr[i-1]:
            return True

    return False







