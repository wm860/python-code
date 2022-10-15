def my_abs(items):
    a=items[0]
    b=items[0]
    aa=0
    bb=0
    for i in range(1,len(items)):
        if items[i]>a:
            aa=i
        if items[i]<b:
            bb=i
    items[aa], items[bb] = items[bb], items[aa]
    return items
if __name__ == "__main__":
    result = sweap([5, 9, 1, 2, 3, 4, 0])
    print(result)