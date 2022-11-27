def sort(items):
    right = len(items)
    run = True
    while run == True:
        for i in right:
            run = False
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1],  items[i]
                run = True
        right -= 1
    return items

if __name__ == "__main__":
    result = sort([90, 5, 4, 3, 2, 1])
    print(result)