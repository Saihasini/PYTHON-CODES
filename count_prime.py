def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
def count(lst):
    if not lst:
        return 0
    return (1 if is_prime(lst[0]) else 0) + count(lst[1:])
numbers = [2, 3, 4, 5, 6, 7, 10, 11]
print("Count of prime numbers:", count(numbers))
