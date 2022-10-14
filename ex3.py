def minmax(items):
    a=items[0]
    b=items[0]
    for i in range(1,len(items)):
        if items[i]>a:
            a=items[i]
        if items[i]<b:
            b=items[i]
    return b,a


if __name__ == "__main__":
    print(minmax([10,1,22,19,30]))
