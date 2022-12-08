"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    prime_numbers = []

    if (number_of_primes <= 0):
        raise ValueError('number must be non-negative')
    else:
        for number in range(2, 100):
            is_prime = all((number % num != 0) for num in range(2, (number)))
            if is_prime:
                prime_numbers.append(number)
            if len(prime_numbers) == number_of_primes:
                break
        return prime_numbers
