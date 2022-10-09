def fi(n):
    cache = {
        0: 0,
        1: 1
    }
    def _fib(n):
        if n not in cache:
            cache[n] = _fib(n-1) + _fib(n-2)
        return cache[n]
    return _fib(n)

if __name__ == "__main__":
    print(fi(100))
