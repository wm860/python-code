if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]

    print(items[:])
    items.append(10)
    print(items[:])

    items.extend([10,11,12])
    print(items[:])

    for i in range(len(items)):
        print(i, items[i])

    for it in items:
        print(it)

    x=10
    while x > 0:
        print(x)
        x=x-1
