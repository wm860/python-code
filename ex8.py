def even1(items):
    return[item for item in items if item %2 == 0]

def even2(items):
    for value in range(len(items)):
        if value % 2 == 0:
            yield value

    return[item for item in range(items) if item %2 == 0]

if __name__ == "__main__":
    result = even1([1, 8, 7, 10, 9, 6, 3])
    for value in even2([1, 8, 7, 10, 9, 6, 3])
        print(value)
    print(result)