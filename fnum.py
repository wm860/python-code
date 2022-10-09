if __name__ == "__main__":
    even_nums = [
        x for x in range(20) if x % 2 == 0
    ]
    values = [
        (x,y)
        for x in range(20)
        for y in range(20)
    ]
    print(values)
