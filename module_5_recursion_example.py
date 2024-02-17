
# Example: Calculating factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
print('Factorial of 5:', factorial(5))

# Example: Generating Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print('Fibonacci sequence up to 5:')
for i in range(6):
    print(fibonacci(i))
