def my_max(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
        return c

if __name__ == "__main__":
    print(my_max(int(input("podaj 1")), int(input("podaj 2")), int(input("podaj 2"))))

