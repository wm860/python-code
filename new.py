def is_prime(n):
    i=3
    if n == 1 or n == 2:
        return True

    for _ in range (n-1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(5))