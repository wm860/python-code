def is_prime(n):
    i=2
    if n == 1:
        return False
    for _ in range (n-2):
        if n%i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    print(is_prime(20))