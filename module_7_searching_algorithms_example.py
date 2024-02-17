
# Example: Linear Search Implementation
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example: Binary Search Implementation
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10
print("Element found at index (Linear Search):", linear_search(arr, x))
print("Element found at index (Binary Search):", binary_search(arr, x))
