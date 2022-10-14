def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def prime_generator(n):
    for i in range(1,n+1):
        if is_prime(i):
            yield i
if __name__ == "__main__":
    for prime in prime_generator(100):
        print(prime)
