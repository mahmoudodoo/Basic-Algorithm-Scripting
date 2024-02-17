
# Sample Solution: Find the Missing Number
def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Sample Solution: Merge Sorted Arrays
def merge_sorted_arrays(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

# Example usage
print("Missing Number:", find_missing_number([3, 0, 1]))
nums1 = [1,2,3,0,0,0]
merge_sorted_arrays(nums1, 3, [2,5,6], 3)
print("Merged Array:", nums1)
