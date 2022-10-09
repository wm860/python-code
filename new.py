def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [
        x for x in range(200) if is_prime(x)
    ]
    print(primes)