def filter_nums(items):
    return[item for item in items if item %3 != 0]

if __name__ == "__main__":
    result = filter_nums([1, 8, 7, 10, 9, 6, 3])
    print(result)
