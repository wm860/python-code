def my_gen(n):
    for i in range(n):
        yield i

def fib(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

if __name__ == "__main__":

    for val in fib(10):
        print(val)
    fib_nums = list(fib(10))
    print(fib_nums)

