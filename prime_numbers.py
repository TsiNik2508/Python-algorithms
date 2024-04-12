def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Пример использования:
minimum = 10
maximum = 30
print(prime_numbers(minimum, maximum))
