
# Example: A simple algorithm to find the maximum number in a list

def find_max(numbers):
    max_num = numbers[0]  # Assume the first number is the max
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

# Example usage
numbers_list = [4, 2, 8, 6, 5]
print(f"The maximum number is: {find_max(numbers_list)}")
