'''Filter out all prime numbers from a list.
 Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 Output: [2, 3, 5, 7]'''
#Here is a Python solution that filters out all prime numbers from a given list:



def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    """Filter out all prime numbers from a list."""
    return [n for n in numbers if is_prime(n)]

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_primes(numbers))

